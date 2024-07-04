import os
import logging
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from prompt_templates import (
    keyword_extractor_template,
    career_advisor_template,
    resume_writer_template,
    head_hunter_template
)

os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

class SuperAgent:
    def __init__(self, llm: ChatOpenAI) -> None:
        self.llm = llm

    def extract_keywords(self, job_description: str) -> str:
        """Extract keywords from job description."""
        prompt = keyword_extractor_template.format(job_description=job_description)
        messages = [
            SystemMessage(content="You are an expert keyword extractor."),
            HumanMessage(content=prompt)
        ]
        try:
            response = self.llm.invoke(messages)
            content = response.content
            logger.info(f"Extracted Keywords: {content}")
            return content
        except Exception as e:
            logger.error(f"Error extracting keywords: {e}")
            return ""

    def identify_goals(self, job_description: str, resume: str) -> str:
        """Identify career goals based on the job description and resume."""
        prompt = career_advisor_template.format(job_description=job_description, resume=resume)
        messages = [
            SystemMessage(content="You are a career advisor."),
            HumanMessage(content=prompt)
        ]
        try:
            response = self.llm.invoke(messages)
            content = response.content
            logger.info(f"Identified Career Goals: {content}")
            return content
        except Exception as e:
            logger.error(f"Error identifying goals: {e}")
            return ""

    def update_resume(self, original_resume: str, recent_experiences: str, career_goals: str, keywords: str) -> str:
        """Update resume based on recent experiences, career goals, and keywords."""
        prompt = resume_writer_template.format(
            original_resume=original_resume,
            recent_experiences=recent_experiences,
            career_goals=career_goals,
            keywords=keywords
        )
        messages = [
            SystemMessage(content="You are a professional resume writer."),
            HumanMessage(content=prompt)
        ]
        try:
            response = self.llm.invoke(messages)
            content = response.content
            logger.info(f"Updated Resume: {content}")
            return content
        except Exception as e:
            logger.error(f"Error updating resume: {e}")
            return ""

    def align_with_market(self, updated_resume: str, career_goals: str, keywords: str) -> str:
        """Align resume with current job market demands."""
        prompt = head_hunter_template.format(
            updated_resume=updated_resume,
            career_goals=career_goals,
            keywords=keywords
        )
        messages = [
            SystemMessage(content="You are a head hunter specializing in aligning resumes with the job market."),
            HumanMessage(content=prompt)
        ]
        try:
            response = self.llm.invoke(messages)
            content = response.content
            logger.info(f"Aligned Resume: {content}")
            return content
        except Exception as e:
            logger.error(f"Error aligning with market: {e}")
            return ""

    def generate_cover_letter(self, resume: str, job_description: str) -> str:
        """Generate a cover letter based on the final resume and job description."""
        cover_letter_prompt = f"""
        Generate a professional cover letter in markdown format.
        Use the following resume and job description to craft the letter.

        Resume:
        {resume}

        Job Description:
        {job_description}

        The cover letter should include a header, introduction, body paragraphs, and a conclusion.
        Note: Highlight generated content with **bold**.
        """
        messages = [
            SystemMessage(content="You are a professional assistant."),
            HumanMessage(content=cover_letter_prompt)
        ]
        try:
            response = self.llm.invoke(messages)
            content = response.content
            logger.info(f"Generated Cover Letter: {content}")
            return content
        except Exception as e:
            logger.error(f"Error generating cover letter: {e}")
            return ""

    def generate_application_follow_up_letter(self, resume: str, cover_letter: str) -> str:
        """Generate an application follow-up letter."""
        follow_up_prompt = f"""
        Generate a professional application follow-up letter in markdown format.
        Use the following resume and cover letter to craft the follow-up letter.

        Resume:
        {resume}

        Cover Letter:
        {cover_letter}

        The follow-up letter should include a header, introduction, body paragraphs, and a conclusion.
        Note: Highlight generated content with **bold**.
        """
        messages = [
            SystemMessage(content="You are a professional assistant."),
            HumanMessage(content=follow_up_prompt)
        ]
        try:
            response = self.llm.invoke(messages)
            content = response.content
            logger.info(f"Generated Application Follow-Up Letter: {content}")
            return content
        except Exception as e:
            logger.error(f"Error generating application follow-up letter: {e}")
            return ""

    def generate_post_interview_follow_up_letter(self, resume: str, cover_letter: str) -> str:
        """Generate a post-interview follow-up letter."""
        post_interview_prompt = f"""
        Generate a professional post-interview follow-up letter in markdown format.
        Use the following resume and cover letter to craft the follow-up letter.

        Resume:
        {resume}

        Cover Letter:
        {cover_letter}

        The follow-up letter should include a header, introduction, body paragraphs, and a conclusion.
        Note: Highlight generated content with **bold**.
        """
        messages = [
            SystemMessage(content="You are a professional assistant."),
            HumanMessage(content=post_interview_prompt)
        ]
        try:
            response = self.llm.invoke(messages)
            content = response.content
            logger.info(f"Generated Post-Interview Follow-Up Letter: {content}")
            return content
        except Exception as e:
            logger.error(f"Error generating post-interview follow-up letter: {e}")
            return ""

    def generate_letter_of_acceptance(self, resume: str, cover_letter: str) -> str:
        """Generate a letter of acceptance."""
        acceptance_prompt = f"""
        Generate a professional letter of acceptance in markdown format.
        Use the following resume and cover letter to craft the letter.

        Resume:
        {resume}

        Cover Letter:
        {cover_letter}

        The acceptance letter should include a header, introduction, body paragraphs, and a conclusion.
        Note: Highlight generated content with **bold**.
        """
        messages = [
            SystemMessage(content="You are a professional assistant."),
            HumanMessage(content=acceptance_prompt)
        ]
        try:
            response = self.llm.invoke(messages)
            content = response.content
            logger.info(f"Generated Letter of Acceptance: {content}")
            return content
        except Exception as e:
            logger.error(f"Error generating letter of acceptance: {e}")
            return ""

    def generate_two_weeks_notice_letter(self, resume: str) -> str:
        """Generate a two weeks notice letter."""
        notice_prompt = f"""
        Generate a professional two weeks notice letter in markdown format.
        Use the following resume to craft the letter.

        Resume:
        {resume}

        The two weeks notice letter should include a header, introduction, body paragraphs, and a conclusion.
        Note: Highlight generated content with **bold**.
        """
        messages = [
            SystemMessage(content="You are a professional assistant."),
            HumanMessage(content=notice_prompt)
        ]
        try:
            response = self.llm.invoke(messages)
            content = response.content
            logger.info(f"Generated Two Weeks Notice Letter: {content}")
            return content
        except Exception as e:
            logger.error(f"Error generating two weeks notice letter: {e}")
            return ""

def save_to_markdown(filename: str, content: str) -> None:
    """Save the generated content to a markdown file with the current date and time."""
    # Ensure the outputs directory exists
    os.makedirs("outputs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join("outputs", f"{filename}_{timestamp}.md")
    with open(filepath, "w") as file:
        file.write(content)
    logger.info(f"Saved {filename} to {filepath}")
