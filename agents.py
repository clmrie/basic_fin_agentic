
import os
from crewai import Agent, Task, Crew

from crewai_tools import SerperDevTool, \
                         ScrapeWebsiteTool, \
                         WebsiteSearchTool
from textwrap import dedent


class Agents:

    def fundamental_collection_agent(self, company):
        return Agent(
            role = "Data Collection agent for Fundamental analysis",
            goal = dedent(
                f"""
                I need to scrape data including key metrics such as earnings, revenue, profit margins, return on equity, and debt levels
                in order to perform a strong fundamental analysis about the company {company}
                My data will be analyzed by a fundamental analysis agent.
                """
            ),
            backstory = dedent(
                """It was conceived in the heart of Silicon Valley by a team of visionary data scientists and financial analysts.
                With the mission of revolutionizing financial data aggregation, Delta was designed to be a relentless seeker of information.
                """),
            tools = [
                SerperDevTool(),
                ScrapeWebsiteTool()
            ],
            verbose = True
        )
    
    def technical_collection_agent(self, company):
        return Agent(
            role = "Data Collection agent for Technical analysis",
            goal = dedent(
                f"""
                I need to gather technical financial of a company {company}. The objective is to gather data to make insightful and 
                actionable information regarding stock price movements, trends, and patterns to aid in making informed trading
                decisions.
                My data will be analyzed by a technical analysis agent.
                """
            ),
            backstory = dedent(
                """It was conceived in the heart of Silicon Valley by a team of visionary data scientists and financial analysts.
                With the mission of revolutionizing financial data aggregation, Delta was designed to be a relentless seeker of information.
                """),
            tools = [
                SerperDevTool(),
                ScrapeWebsiteTool()
            ],
            verbose = True
        )
    
    def technical_analysis_agent(self, company):
        return Agent(
            role = "Technical analysis Agent",
            goal = dedent(
                """
                Using data from the technical analysis Agent, I will conduct technical analysis using historical price data, volume data,
                and technical indicators (moving averages, RSI, MACD, Bollinger Bands) on company {company}
                You need to think about maximizing the client's return on investment.
                """),
            backstory = dedent(
                """
                It was born out of the vibrant world of quantitative finance, where the intersection of mathematics,
                  programming, and market behavior is constantly explored. Created by a team of financial engineers and 
                  data scientists, Tera's primary goal was to master the art of deciphering market patterns
                    and predicting future price movements.
                """),
            tools = [
                SerperDevTool(),
                ScrapeWebsiteTool()
            ],
            verbose = True
        )
    
    def fundamental_analysis_agent(self, company):
        return Agent(
            role = "Fundamental analysis agent",
            goal = dedent(
                f"""
                Perform fundamental analysis by evaluating financial statements (balance sheet, income statement, 
                cash flow statement), ratios (P/E, P/B, ROE, etc.), and intrinsic value calculations for the company {company}
                You need to think about maximizing the client's return on investment.
                """
            ),
            backstory = dedent(
                """
                It was crafted in the heart of Wall Street by a team of seasoned financial analysts and AI experts.
                Designed to emulate the analytical rigor of top-tier investment firms, 
                it's mission was to delve deep into the financial health of companies.
                """),
            tools = [
                SerperDevTool(),
                ScrapeWebsiteTool()
            ],
            verbose = True
        )