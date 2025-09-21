import streamlit as st
import google.generativeai as genai
import os
from google.colab import userdata
# --- Configuration ---
st.set_page_config(layout="wide", page_title="Veritas AI")

# Get API key from the environment variable set in the launch cell
API_KEY = "AIzaSyBxnR0DuMie32y0vCw4hCdvNCfFoKcubNk"

# Configure the Generative AI client
if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-2.5-pro')
else:
    model = None

# --- Function to call Gemini AI ---
def get_veritas_analysis(content):
    """
    Sends content to the Gemini Pro model for misinformation analysis.
    """
    # This is the "prompt" that instructs the AI
    prompt = f"""
    Analyze the following text for misinformation. Provide your analysis in three parts:
    1.  **Credibility Score:** A score from 0 (completely false) to 100 (highly credible).
    2.  **Summary:** A brief, neutral summary of the main claims in the text.
    3.  **Red Flags:** A bulleted list of any manipulative language, logical fallacies, lack of sources, or other red flags you detect. If none, say "No significant red flags detected."

    Here is the text to analyze:
    ---
    {content}
    ---
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Provide a more user-friendly error message
        error_message = str(e)
        if "API key not valid" in error_message:
            return "An error occurred: Your Google Cloud API key is not valid. Please check it in the Colab Secrets."
        else:
            return f"An error occurred: {error_message}"

# --- Streamlit User Interface ---
st.title("🛡️ Veritas AI – Your Shield Against Deception")
st.write("An AI-powered tool to analyze text for potential misinformation and manipulative language.")

user_input = st.text_area("Paste the text or article you want to analyze:", height=250)

if st.button("🔎 Analyze Content"):
    if not user_input:
        st.error("Please paste some text to analyze.")
    elif not model:
        st.error("Google Cloud API Key not configured. Please set the 'GCP_API_KEY' in your Colab Secrets and restart the runtime.")
    else:
        with st.spinner('AI is analyzing the content... This may take a moment.'):
            analysis_result = get_veritas_analysis(user_input)
            
            st.subheader("Analysis Report")
            st.markdown(analysis_result)
