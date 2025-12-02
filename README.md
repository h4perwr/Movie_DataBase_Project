# Movie_DataBase_Project
The project for DataBase course with AI integration

## Project Overview
### This project focuses on the design, development, and implementation of a robust AI-powered Text-to-SQL Agent for a large-scale relational database. The solution automates complex data analysis by translating natural language queries into optimized SQL, delivering structured business insights for a fictional movie studio.

### The core achievement lies in the successful integration of advanced Database Engineering practices (Normalization, Indexing) with modern AI Engineering tools (LangChain, Gemini) to ensure performance, security, and scalability.

# Area,Achievement,Metric / Impact
Data Architecture,Built a fully normalized relational database (3NF).,"Successfully migrated and structured a large raw dataset containing 200,000+ rows."
Performance,Implemented Database Optimization techniques.,Achieved efficient query performance through Indexing on critical foreign keys and creating Analytical VIEWs.
AI Integration,Developed a specialized Text-to-SQL Agent.,Utilized LangChain with Gemini-2.5-Flash to autonomously analyze data and generate insights.
Security & Auditing,Implemented critical security Guardrails.,"Agent execution is strictly limited to SELECT operations; dangerous DML/DDL commands (INSERT, UPDATE, DROP) are programmatically blocked via the system prompt."
Analytics,Prepared the foundation for complex SQL Analytics and AI Modeling.,Created optimized analytical VIEWs and feature sets necessary for revenue optimization and rating prediction models.


# Solved Business Problems
## The agent is trained to address the following high-value analytical questions for the studio:
-- Movie Revenue Optimization: Determine which factors (Genre, Budget, Director) exert the strongest influence on global box office performance.
-- Director Performance Evaluation: Identify directors who consistently deliver high-performing films in terms of both ratings and revenue.
-- Genre Profitability Analysis: Quantify the Return on Investment (ROI) by comparing budgets and revenues across various movie genres.
-- Rating Prediction: Prepared the integrated dataset required to predict audience satisfaction (IMDb/RT scores) based on pre-production metadata.
