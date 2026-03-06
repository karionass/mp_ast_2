import streamlit as st
from src.crew import crew

st.set_page_config(page_title="Локализация лекций", layout="wide")
st.title("Локализация и адаптация учебного видеоконтента")

# --- Зона 1: Конфигурация ---
st.header("Конфигурация агентов")
role_transcriber = st.text_input("Role Transcriber", "Анализирует исходный текст лекции")
goal_transcriber = st.text_input("Goal Transcriber", "Преобразовать англоязычный транскрипт")
backstory_transcriber = st.text_area("Backstory Transcriber", "Опытный специалист по обработке текста...")

role_localizer = st.text_input("Role Localizer", "Локализует и адаптирует контент")
goal_localizer = st.text_input("Goal Localizer", "Перевести лекцию на русский язык")
backstory_localizer = st.text_area("Backstory Localizer", "Педагог и лингвист...")

# --- Зона 2: Ввод данных ---
st.header("Ввод данных")
transcript_file = st.file_uploader("Загрузите транскрипт лекции", type="txt")
glossary_file = st.file_uploader("Загрузите глоссарий", type="txt")

# --- Зона 3: Запуск и визуализация ---
if st.button("Запустить Crew") and transcript_file and glossary_file:
    transcript = transcript_file.read().decode("utf-8")
    glossary = glossary_file.read().decode("utf-8")
    
    inputs = {"transcript": transcript, "glossary": glossary}
    
    crew = crew.Crew("agents.yaml", "tasks.yaml", inputs)
    results = crew.run()
    
    st.subheader("Результаты локализации")
    for block in results:
        st.markdown(f"**Блок {block['block']}**: {block['translated_text']}")