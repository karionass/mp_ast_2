from crewai import Agent
import yaml
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AGENTS_PATH = os.path.join(BASE_DIR, "config", "agents.yaml")


def load_agents():
    with open(AGENTS_PATH, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    agents = {}

    for name, data in config.items():
        agents[name] = Agent(
            role=data["role"],
            goal=data["goal"],
            backstory=data["backstory"],
            verbose=True
        )

    return agents