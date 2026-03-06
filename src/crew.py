from crewai import Agent, Task, Crew
import os
from dotenv import load_dotenv
from crewai import LLM, Agent

load_dotenv()
os.getenv("GOOGLE_API_KEY")

llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)

def run_crew(transcript: str, glossary: str):
    """
    Создаём двух агентов и выполняем задачи локализации.
    Проверяем, что текст и глоссарий не пустые.
    """
    transcript = transcript.strip()
    glossary = glossary.strip()

    if not transcript:
        raise ValueError("Текст лекции пустой!")
    if not glossary:
        raise ValueError("Глоссарий пустой!")

    # --- Агенты ---
    transcriber = Agent(
        role="Lecture Analyzer",
        goal="Разбить текст лекции на блоки",
        backstory="Специалист по обработке текста",
        llm=llm
    )

    localizer = Agent(
        role="Content Localizer",
        goal="Перевести лекцию с глоссарием",
        backstory="Лингвист",
        llm=llm
    )

    # --- Задачи ---
    task1 = Task(
        description=f"Разбей текст лекции на блоки:\n{transcript}",
        agent=transcriber
    )

    task2 = Task(
        description=f"Переведи текст с использованием глоссария:\n{glossary}",
        agent=localizer
    )

    # --- Экипаж ---
    crew = Crew(
        agents=[transcriber, localizer],
        tasks=[task1, task2]
    )

    # --- Запуск ---
    result = crew.kickoff()
    return result