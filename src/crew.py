from crewai import Agent, Task, LLM

llm = LLM(model="gemini/gemini-1.5-flash", api_key="ВАШ_API_KEY")

agent = Agent(
    role="Test",
    goal="Test goal",
    backstory="Test backstory",
    llm=llm
)

task = Task(
    description="Test task",
    agent=agent
)

print(task)