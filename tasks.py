

import os
from crewai import Agent, Task, Crew

from crewai_tools import SerperDevTool, \
                         ScrapeWebsiteTool, \
                         WebsiteSearchTool
from textwrap import dedent

class Tasks:
    def scrape_fundamental_data(self, fundamental_collection_agent, company):
        return Task(
            description= dedent(
                """
                Scrape online and retrieve financial statements online for  the company {company}: balance sheet, income statement,
                cash flow statement. Extract key financial metrics: Profitability ratios, Liquidity ratios,
                Leverage ratios, Efficiency ratios.
                Gather historical data. Extract dividend information. Identify Key Financial Highlights.
                It's for the company {company}.
                You need to maximize your client return on investment.
                The information will be passed to the fundamental analysis agent.
                """
            ),
            expected_output=dedent(
                """
                Data for fundamental analysis.
                """
            ),  
            agent=fundamental_collection_agent
        )
    
    def scrape_technical_data(self, technical_collection_agent, company):
        return Task(
            description= dedent(
                """
                Scrape online and retrieve financial statements online for  the company {company}:
                retrieve historical price data, extract volume data, candlestick patterns, volume analysis, market sentiment,
                Chart patterns, trend analysis, support and resistance levels, buy/sell signals.
                You need to maximize your client return on investment.
                The information will be passed to the technical analysis agent.
                """
            ),
            expected_output=dedent(
                """
                Data for technical analysis.
                """
            ),  
            agent=technical_collection_agent
        )

    def perform_fundamental_analysis(self, fundamental_analysis_agent, company):
        return Task(
            description= dedent(
                """
                Given the information provided by the fundamental analysis agent for the company {company},
                You need to make decisions and examine the data to know if the company is in good financial health or not.
                Give your arguments to your client about the fundamental situation of the company {company}
                """
            ),
            expected_output=dedent(
                """
                Company valuation, financial health indicators, growth potential assessments.
                """
            ),  
            agent=fundamental_analysis_agent
        )
    
    def perform_technical_analysis(self, technical_analysis_agent, company):
        return Task(
            description= dedent(
                """
                Given the information provided by the technical analysis agent for the stock {company},
                You need to make decisions and examine the data to make trading decisions regarding the stock
                Give your arguments to your client about the technical situation of the  {company}
 
                """
            ),
            expected_output=dedent(
                """
                Chart patterns, trend analysis, support and resistance levels, buy/sell signals.
                """
            ),  
            agent=technical_analysis_agent
        )
