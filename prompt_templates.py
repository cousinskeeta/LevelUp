from langchain_core.prompts import PromptTemplate

# Keyword Extractor Prompt Template
keyword_extractor_template = PromptTemplate(
    input_variables=["job_description"],
    template="""
    Input: Extract key words and phrases from the job description provided.
    Context: This job description is for a senior data engineer role in a tech company. Identify technical skills, soft skills, and specific experiences required.
    Examples:
    Job Description: "We need a senior data engineer with experience in cloud computing, large-scale data processing, and Python."
    Extracted Keywords: ["cloud computing", "large-scale data processing", "Python"]
    Task: Extract keywords from the following job description: {job_description}
    """
)

# Career Advisor Prompt Template
career_advisor_template = PromptTemplate(
    input_variables=["job_description", "resume"],
    template="""
    Act as a Career Advisor who specializes in identifying career goals and relevant roles based on job descriptions.
    The candidate is aiming for a senior position in the tech industry. Focus on goals that align with the responsibilities and requirements in the job description.
    Examples:
    Job Description: "Looking for a senior data engineer with leadership experience, expertise in data pipeline development, and knowledge of machine learning."
    Career Goals: ["Lead data engineering projects", "Develop advanced data pipelines", "Integrate machine learning models"]
    Task: Identify career goals and relevant roles from the following job description: {job_description}; as well as the candidate's resume: {resume}
    Note: Highlight generated content with **bold**.
    """
)

# Resume Writer Prompt Template
resume_writer_template = PromptTemplate(
    input_variables=["original_resume", "recent_experiences", "career_goals", "keywords"],
    template="""
    Act as a resume writer. Update the candidate's resume based on their recent experiences, career goals of the desired job, and keywords.
    The original resume needs enhancement to highlight recent achievements, align with career goals, and include relevant keywords. Use a professional tone and structure.
    Examples:
    Original Resume: "Experienced data engineer with expertise in various data tools."
    Recent Experiences: "Led a team to develop a cloud-based data pipeline."
    Career Goals: "Lead data engineering projects, integrate machine learning models."
    Keywords: ["cloud-based", "data pipeline", "machine learning"]
    Updated Resume: "Senior Data Engineer with expertise in cloud-based data pipelines and machine learning. **Led a team to develop scalable solutions, achieving a 20% improvement in processing efficiency.**"
    Task: Generate the updated resume based on the following information: {original_resume} {recent_experiences} {career_goals} {keywords}
    Note: Highlight generated content with **bold**.
    """
)

# Head Hunter Prompt Template
head_hunter_template = PromptTemplate(
    input_variables=["updated_resume", "career_goals", "keywords"],
    template="""
    Act as a tech head hunter that aligns candidate resumes with current job market demands considering career goals and keywords.
    The candidate's resume needs to stand out to recruiters by showcasing relevant skills and experiences that are in demand in the tech industry.
    Examples Must Have:
        Contact: Name, Phone, Email (Optional: Portfolio Link)
        Summary: Briefly tell me your tech skills and goals (1-3 sentences).
        Experience: List jobs (newest first). Use strong verbs to describe what you did and achieved (quantify results if possible).
        Skills: List your programming languages, tools, and technologies.
    Optional But Great:
        Education: Degrees, School, Year (mention relevant coursework)
        Certifications: Any certifications that boost your skills
    Task: Generate the final resume with market demands based on the following information: {updated_resume} {career_goals} {keywords}
    Note: Highlight generated content with **bold**.
    """
)
