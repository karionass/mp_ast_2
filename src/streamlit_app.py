# src/streamlit_app.py
import streamlit as st
from crew import run_crew  # функция из crew.py

st.set_page_config(page_title="Локализация контента", layout="wide")
st.title("Локализация и адаптация учебного видеоконтента")


st.header("Конфигурация агентов")

role_transcriber = st.text_input("Role Transcriber", "Анализирует исходный текст видеоконтента")
goal_transcriber = st.text_input("Goal Transcriber", "Преобразовать англоязычный транскрипт")
backstory_transcriber = st.text_area("Backstory Transcriber", "Опытный специалист по обработке текста")

role_localizer = st.text_input("Role Localizer", "Локализует и адаптирует контент")
goal_localizer = st.text_input("Goal Localizer", "Перевести лекцию на русский язык")
backstory_localizer = st.text_area("Backstory Localizer", "Преподаватель и лингвист, занимающийся локализацией образовательного контента")


st.header("Ввод данных")

transcript_file = st.file_uploader("Загрузите транскрипт лекции", type="txt")
glossary_file = st.file_uploader("Загрузите глоссарий", type="txt")

st.header("Или введите текст лекции и глоссария")
transcript_text = st.text_area("Вставьте текст лекции на английском", height=200)
glossary_text = st.text_area("Вставьте глоссарий (каждый термин — перевод, одну пару на строку)", height=150)


if st.button("Запуск"):
    if transcript_file:
        transcript = transcript_file.read().decode("utf-8")
    else:
        transcript = transcript_text

    if glossary_file:
        glossary = glossary_file.read().decode("utf-8")
    else:
        glossary = glossary_text

    if not transcript or not glossary:
        st.warning("Пожалуйста, загрузите файлы или введите текст вручную!")
    else:
        with st.spinner("Анализ и локализация..."):
            results = run_crew(transcript, glossary)

        st.subheader("Результат локализации")
        for i, block in enumerate(results, 1):
            st.markdown(f"**Блок {i}**: {block.get('translated_text', block)}")