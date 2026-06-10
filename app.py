import streamlit as st
from deep_translator import GoogleTranslator
import pyperclip

st.set_page_config(page_title="Language Translator", page_icon="🌍")

st.title("🌍 Language Translation Tool")

languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

source_lang = st.selectbox(
    "Select Source Language",
    list(languages.keys())
)

target_lang = st.selectbox(
    "Select Target Language",
    list(languages.keys())
)

text = st.text_area("Enter Text")

if st.button("Translate"):
    if text:
        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("Translation Completed!")

        st.text_area(
            "Translated Text",
            translated,
            height=150
        )

        if st.button("Copy Translation"):
            pyperclip.copy(translated)
            st.success("Copied Successfully!")
    else:
        st.warning("Please enter text to translate.")
