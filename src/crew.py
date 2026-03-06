from crewai import Agent, Task, Crew
import os
from dotenv import load_dotenv
from crewai import LLM, Agent

load_dotenv()
os.getenv("GOOGLE_API_KEY")

llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
)

def run_crew(transcript: str, glossary: str):
    if not transcript or not glossary:
        raise ValueError("Заполните оба поля: транскрипт и глоссарий")

    llm = LLM(model="gemini/gemini-1.5-flash", api_key=os.getenv("GOOGLE_API_KEY"))

    transcriber = Agent(
        role="Lecture Analyzer",
        goal="Разбить лекцию на блоки",
        backstory="Специалист по обработке текста",
        llm=llm
    )

    localizer = Agent(
        role="Content Localizer",
        goal="Перевести лекцию с глоссарием",
        backstory="Лингвист",
        llm=llm
    )

    transcript = transcript.strip()
    glossary = glossary.strip()

    task1 = Task(
        description=f"Разбей текст лекции на блоки:\n{transcript}",
        agent=transcriber,
        expected_output="JSON с логическими блоками текста и ключевыми терминами"
    )

    task2 = Task(
        description=f"Переведи текст с использованием глоссария:\n{glossary}",
        agent=localizer,
        expected_output="JSON с переведённым текстом каждого блока"
    )

    crew = Crew(
        agents=[transcriber, localizer],
        tasks=[task1, task2]
    )

    result = crew.kickoff()
    return result