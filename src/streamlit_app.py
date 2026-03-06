import streamlit as st

st.set_page_config(page_title="Локализация контента", layout="wide")
st.title("Локализация и адаптация учебного видеоконтента")

st.header("Конфигурация агентов")
role_transcriber = st.text_input("Role Transcriber", "Анализирует исходный текст видеоконтента")
goal_transcriber = st.text_input("Goal Transcriber", "Преобразовать англоязычный транскрипт")
backstory_transcriber = st.text_area("Backstory Transcriber", "Опытный специалист по обработке текста")

role_localizer = st.text_input("Role Localizer", "Локализует и адаптирует контент")
goal_localizer = st.text_input("Goal Localizer", "Перевести лекцию на русский язык")
backstory_localizer = st.text_area("Backstory Localizer", "Преподаватель и лингвист занимающийся локализацией образовательного контента")

st.header("Ввод данных")
transcript_file = st.file_uploader("Загрузите транскрипт лекции", type="txt")
glossary_file = st.file_uploader("Загрузите глоссарий", type="txt")
st.header("Или введите текст лекции и глоссария")

transcript = st.text_area(
    "Вставьте текст лекции на английском",
    height=200
)

glossary = st.text_area(
    "Вставьте глоссарий (каждый термин с переводом через тире, одну пару на строку)",
    height=150
)

if st.button("Запуск") and transcript_file and glossary_file:
    transcript = transcript_file.read().decode("utf-8")
    glossary = glossary_file.read().decode("utf-8")
    
    inputs = {"transcript": transcript, "glossary": glossary}
    
    crew = crew.Crew("agents.yaml", "tasks.yaml", inputs)
    results = crew.run()
    
    st.subheader("Результат")
    for block in results:
        st.markdown(f"**Блок {block['block']}**: {block['translated_text']}")