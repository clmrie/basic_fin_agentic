import os
os.environ["OPENAI_MODEL_NAME"] = ''
os.environ["SERPER_API_KEY"] = ''
os.environ['OPENAI_API_KEY'] =''

from crewai import Agent, Task, Crew

from crewai_tools import SerperDevTool, \
                         ScrapeWebsiteTool, \
                         WebsiteSearchTool

from agents import Agents
from tasks import Tasks

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()


class FinCrew:

    def __init__(self, company_name):
        agents = Agents()
        tasks = Tasks()

        # Agents
        fundamental_collection_agent = agents.fundamental_collection_agent(company_name)
        technical_collection_agent = agents.technical_collection_agent(company_name)
        fundamental_analysis_agent = agents.fundamental_analysis_agent(company_name)
        technical_analysis_agent = agents.technical_analysis_agent(company_name)

        # Tasks
        scrape_fundamental_data_task = tasks.scrape_fundamental_data(fundamental_collection_agent, company_name)
        scrape_technical_data_task = tasks.scrape_technical_data(technical_collection_agent, company_name)
        perform_fundamental_analysis = tasks.perform_fundamental_analysis(fundamental_analysis_agent, company_name)
        perform_technical_analysis = tasks.perform_technical_analysis(technical_analysis_agent, company_name)

        crew = Crew(
            agents=[
                fundamental_collection_agent,
                technical_collection_agent,
                fundamental_analysis_agent,
                technical_analysis_agent
                ],
            tasks=[
                scrape_fundamental_data_task,
                scrape_technical_data_task,
                perform_fundamental_analysis,
                perform_technical_analysis
                ],
            verbose=2,
            memory=True
        )
        crew.kickoff({"company": company_name})









if __name__ == "__main__":
    print("\n")
    print("Welcome to the Financial Analysis Agentic Tool ✨")

    input = input("Please enter the name of the company you'd like to analyze:\n")
    fin_crew = FinCrew(input)