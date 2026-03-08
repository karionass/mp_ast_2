from crewai import Crew
from .agents import load_agents
from .tasks import load_tasks


def run_crew(transcript, glossary):

    agents = load_agents()
    tasks = load_tasks(agents)

    # подставляем данные
    tasks[0].description = tasks[0].description.format(transcript=transcript)
    tasks[1].description = tasks[1].description.format(glossary=glossary)

    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()

    return result