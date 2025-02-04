import openai
import streamlit as st

# Title and Description
st.title("Language Translator")
st.write("Translate English text into other languages using OpenAI's API.")

# Load the API key from Streamlit secrets
api_key = st.secrets.get("OPENAI_API_KEY")

if not api_key:
    st.error("API key not found. Please set the OPENAI_API_KEY in Streamlit secrets.")
    st.stop()

openai.api_key = api_key

# Define the translation function
def translate_text(text, target_language):
    prompt = f"Translate the following English text to {target_language}:\n\n{text}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the latest GPT-3.5 model
            messages=[
                {"role": "system", "content": "You are a helpful translator."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100,
            temperature=0.5,
        )
        translation = response.choices[0].message['content'].strip()
        return translation
    except Exception as e:
        st.error(f"An error occurred during translation: {str(e)}")
        return None

# Streamlit App Interface
text = st.text_area("Enter the English text you want to translate")
target_language = st.selectbox("Select the target language", ["French", "Spanish", "German", "Italian"])

if st.button("Translate"):
    if text:
        with st.spinner('Translating...'):
            translation = translate_text(text, target_language)
            if translation:
                st.success(f"Translated Text ({target_language}):")
                st.write(translation)
    else:
        st.warning("Please enter text to translate.")
