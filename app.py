import os
import streamlit as st
from streamlit_lottie import st_lottie
from dotenv import load_dotenv
from super_agent import SuperAgent, save_to_markdown, ChatOpenAI
import json

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def main():
    st.title("LevelUp - Professional Resume and Cover Letter Generator")

    if os.path.exists(".env"):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        org_key = os.getenv("ORG_KEY")
    else:
        api_key = st.text_input("Enter your OpenAI API Key:")
        org_key = st.text_input("Enter your OpenAI ORG Key")
        if api_key and org_key:
            with open(".env", "w") as f:
                f.write(f"OPENAI_API_KEY={api_key}\n")
                f.write(f"ORG_KEY={org_key}\n")

    if api_key and org_key:
        llm = ChatOpenAI(model="gpt-4o", api_key=api_key, organization=org_key)
        agent = SuperAgent(llm=llm)

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Submit", "Results"])

    if page == "Home":
        st.header("Welcome to LevelUp")
        lottie_animation_path = os.path.join(os.getcwd(), "assets", "welcome_animation.json")
        lottie_animation = load_lottiefile(lottie_animation_path)
        st_lottie(lottie_animation, loop=True, height=900, width=600)

    elif page == "Submit":
        st.header("Submit Your Information")
        original_resume = st.text_area("Original Resume")
        recent_experiences = st.text_area("Recent Experiences")
        job_description = st.text_area("Job Description")
        if st.button("Process Resume"):
            if original_resume and recent_experiences and job_description:
                with st.spinner("Processing..."):
                    keywords = agent.extract_keywords(job_description)
                    career_goals = agent.identify_goals(job_description, original_resume)
                    updated_resume = agent.update_resume(original_resume, recent_experiences, career_goals, keywords)
                    final_resume = agent.align_with_market(updated_resume, career_goals, keywords)
                    cover_letter = agent.generate_cover_letter(final_resume, job_description)
                    application_follow_up = agent.generate_application_follow_up_letter(final_resume, cover_letter)
                    post_interview_follow_up = agent.generate_post_interview_follow_up_letter(final_resume, cover_letter)
                    letter_of_acceptance = agent.generate_letter_of_acceptance(final_resume, cover_letter)
                    two_weeks_notice = agent.generate_two_weeks_notice_letter(final_resume)

                    save_to_markdown("final_resume", final_resume)
                    save_to_markdown("cover_letter", cover_letter)
                    save_to_markdown("application_follow_up", application_follow_up)
                    save_to_markdown("post_interview_follow_up", post_interview_follow_up)
                    save_to_markdown("letter_of_acceptance", letter_of_acceptance)
                    save_to_markdown("two_weeks_notice", two_weeks_notice)

                    st.session_state["results"] = {
                        "Final Resume": final_resume,
                        "Cover Letter": cover_letter,
                        "Application Follow-Up Letter": application_follow_up,
                        "Post-Interview Follow-Up Letter": post_interview_follow_up,
                        "Letter of Acceptance": letter_of_acceptance,
                        "Two Weeks Notice Letter": two_weeks_notice,
                    }
                    st.success("Resume processed successfully!")
            else:
                st.error("Please fill in all fields.")

    elif page == "Results":
        st.header("Results")
        if "results" in st.session_state:
            results = st.session_state["results"]
            for title, content in results.items():
                st.subheader(title)
                st.markdown(content)
        else:
            st.write("No results to display. Please submit your information first.")

if __name__ == "__main__":
    main()
