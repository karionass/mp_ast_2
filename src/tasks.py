from crewai import Task
import yaml
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_PATH = os.path.join(BASE_DIR, "config", "tasks.yaml")


def load_tasks(agents):
    with open(TASKS_PATH, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    tasks = []

    for name, data in config.items():
        task = Task(
            description=data["description"],
            agent=agents[data["agent"]],
            expected_output=data["expected_output"]
        )

        tasks.append(task)

    return tasks