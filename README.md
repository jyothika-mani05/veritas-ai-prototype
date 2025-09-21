# Veritas AI - Your Shield Against Deception

## Project Description

Veritas AI is an innovative, AI-powered tool designed to combat the rapid spread of misinformation online. Leveraging Google's Gemini AI, our web application (built with Streamlit) provides users with instant, actionable insights into the credibility of any text content they encounter. From social media posts to news articles, Veritas AI helps you discern fact from fiction.

## Problem Statement

In today's digital age, misinformation and fake news propagate at an alarming rate, eroding public trust and having real-world consequences. With the advent of advanced Generative AI, identifying misleading content, including hyper-realistic deepfakes, has become increasingly challenging for the average internet user. Existing solutions are often slow, inaccessible, or lack the nuance required to keep pace with evolving deceptive tactics.

## Our Solution

Veritas AI tackles this problem head-on by offering:
* **Instant Credibility Analysis:** Our core feature uses Gemini AI to evaluate text and provide a credibility score (0-100%) within seconds.
* **Identified Red Flags:** It highlights manipulative language, logical fallacies, and other common 'red flags' used in misinformation, providing transparency into the AI's assessment.
* **Accessibility:** Designed as a user-friendly Streamlit web application, Veritas AI makes sophisticated misinformation detection accessible to everyone.

## Features

* **Text Analysis:** Paste any text content for AI-driven credibility assessment.
* **Credibility Score:** Get a clear numerical score indicating the likelihood of the content being credible.
* **Highlighted Red Flags:** Visually identify specific words and phrases commonly associated with misinformation.
* **Gemini Pro Integration:** Powered by Google's state-of-the-art Gemini Pro model for nuanced understanding and robust analysis.

## Live Demo

Experience Veritas AI live!
**[](https://veritas-ai-prototype.streamlit.app)** ## Getting Started (Local Development)

To run Veritas AI on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/jyothika-mani05/veritas-ai-prototype.git](https://github.com/jyothika-mani05/veritas-ai-prototype.git)
    cd veritas-ai-prototype
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows: .\venv\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up API Key:**
    * Obtain a Google Cloud API Key for Gemini.
    * Create a `.env` file in the root of your project:
        ```
        GCP_API_KEY="YOUR_GOOGLE_CLOUD_API_KEY"
        ```
    * Make sure `.env` is in your `.gitignore` file.
5.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

## Future Scope

* **Image-based Analysis (OCR):** Extract and analyze text directly from uploaded images and screenshots.
* **Multi-language Support:** Expand analysis capabilities to various languages beyond English.
* **Browser Extension:** Develop a browser extension for seamless, on-the-fly analysis of web content.

## Technologies Used

* **Frontend:** Streamlit
* **AI Model:** Google Gemini 2.5 Pro
* **Deployment:** Streamlit Community Cloud
* **Version Control:** Git & GitHub
* **Python Libraries:** `google-generativeai`, `streamlit`, `python-dotenv`

## Team

* Brindavan Jyothika Mani
* Kancharla Shresta Reddy 
* Chikkala Greeshma
* Pulukuri Sharon

