import streamlit as st
from crew import run_crew
import os

os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]


st.title("Lecture Analyzer")

transcript = st.text_area("Текст лекции")
glossary = st.text_area("Глоссарий")

if st.button("Запустить анализ"):

    result = run_crew(transcript, glossary)

    st.write(result)