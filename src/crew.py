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

def run_crew(transcript, glossary):

    transcriber = Agent(
        role="Lecture Analyzer",
        goal="Разбить транскрипт лекции на блоки по смыслу",
        backstory="Специалист по анализу учебного контента",
        llm=llm
    )

    localizer = Agent(
        role="Content Localizer",
        goal="Перевести лекцию и применить глоссарий терминов",
        backstory="Эксперт по локализации образовательного контента",
        llm=llm
    )

    task1 = Task(
        description=f"""
        Разбей следующий транскрипт лекции на блоки по смыслу:

        {transcript}
        """,
        agent=transcriber
    )

    task2 = Task(
        description=f"""
        Используя глоссарий:

        {glossary}

        Переведи и адаптируй текст лекции:

        {transcript}
        """,
        agent=localizer
    )

    crew = Crew(
        agents=[transcriber, localizer],
        tasks=[task1, task2]
    )

    result = crew.kickoff()
    return result