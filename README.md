# LevelUp - Professional Resume and Cover Letter Generator

![LevelUp Logo](assets/logo.png)

## Overview

LevelUp is an AI-powered application that helps users generate professional resumes, cover letters, and follow-up letters using the LangChain framework and OpenAI's GPT-4o model. The application aims to streamline the job application process, providing users with tailored and polished documents.

## Features

- **Resume Enhancement**: Update and enhance your resume based on recent experiences, career goals, and job descriptions.
- **Cover Letter Generation**: Automatically generate a professional cover letter tailored to the job description and your resume.
- **Follow-Up Letters**: Create application follow-up letters, post-interview follow-up letters, letters of acceptance, and two weeks' notice letters.
- **Markdown Output**: Save all generated documents in markdown format for easy editing and sharing.
- **User-Friendly Interface**: Easy-to-use Streamlit interface for users of all technical backgrounds.

## Installation

### Prerequisites

- Python 3.9 or higher
- OpenAI API key

### Clone the Repository

```bash
git clone https://github.com/cousinskeeta/LevelUp
cd LevelUp
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the project root directory with the following content:

```makefile
OPENAI_API_KEY=your_openai_api_key
ORG_KEY=your_org_id_key
```

## Usage

### Run the Application

```bash
streamlit run app.py
```

### Submit Your Information

1. Go to the "Submit" section.
2. Enter your original resume, recent experiences, and job description.
3. Click "Process Resume" to generate the documents.
4. View and download the generated documents from the "Results" section.

## Project Structure

```graphql
LevelUp/
├── assets/                         # Contains logo and other static files
├── outputs/                        # Directory where generated markdown files are saved
├── logs/                           # Directory for log files
├── super_agent.py                  # Main logic for interacting with the LLM and generating documents
├── app.py                          # Streamlit app script
├── prompt_templates.py             # Prompt templates used for generating responses
├── requirements.txt                # Python dependencies
└── .env.example                    # Example environment variables file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI](https://www.openai.com/)
- [Streamlit](https://www.streamlit.io/)

## Contact

For any questions or suggestions, please open an issue or [Buy Me A Coffe](https://www.buymeacoffee.com/jacobtadesse).
