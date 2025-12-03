# Movie_DataBase_Project
The project for DataBase course with AI integration

## 1. Project Overview

This project focuses on the design, development, and implementation of a robust **AI-powered Text-to-SQL Agent** for a large-scale relational database. The solution automates complex data analysis by translating natural language queries into optimized SQL, delivering structured business insights for a fictional movie studio.

The core achievement lies in the successful integration of advanced **Database Engineering** practices (Normalization, Indexing) with modern **AI Engineering** tools (LangChain, Gemini) to ensure performance, security, and scalability.

---

## 2. Key Achievements & Engineering Highlights

| Area | Achievement | Metric / Impact |
| :--- | :--- | :--- |
| **Data Architecture** | Built a **fully normalized relational database** (3NF). | Successfully migrated and structured a large raw dataset containing **200,000+ rows**. |
| **Performance** | Implemented **Database Optimization** techniques. | Achieved efficient query performance through **Indexing** on critical foreign keys and creating **Analytical VIEWs**. |
| **AI Integration** | Developed a specialized **Text-to-SQL Agent**. | Utilized **LangChain** with **Gemini-2.5-Flash** to autonomously analyze data and generate insights. |
| **Security & Auditing** | Implemented critical security **Guardrails**. | Agent execution is strictly limited to its defined role **programmed manualy** |
| **Analytics** | Prepared the foundation for complex **SQL Analytics and AI Modeling**. | Created **optimized analytical VIEWs** and feature sets necessary for revenue optimization and rating prediction models. |

---

## 3. Solved Business Problems

The agent is trained to address the following high-value analytical questions for the studio:

1.  **Movie Revenue Optimization:** Determine which factors (Genre, Budget, Director) exert the **strongest influence on global box office performance**.
2.  **Director Performance Evaluation:** Identify directors who **consistently** deliver high-performing films in terms of both ratings and revenue.
3.  **Genre Profitability Analysis:** Quantify the **Return on Investment (ROI)** by comparing budgets and revenues across various movie genres.
4.  **Rating Prediction:** Prepared the integrated dataset required to predict audience satisfaction (IMDb/RT scores) based on pre-production metadata.

---

## 4. Technology Stack

* **Database:** MySQL
* **AI/LLM:** Gemini 2.5 Flash
* **Framework:** LangChain (1.x)
* **Language:** Python 3.10+

---

## 5. Installation and Execution

To run the AI Agent successfully, follow these steps to set up the environment and database.

### 5.1. Database Setup (MySQL Workbench)
It would be better to have your own dataset. You could find it on whether on Kaggle or make it yourself.

### 5.2. Python Environment Configuration
1. **Setup virtual environment and activativation**
   ```bash
   python -m venv venv
   ```
   
   # *In Windows:*
   ```bash
   ./venv/Scripts/activate
   ```

   # In Linux:
   ```bash
   source ./venv/bin/activate
   ```
   
2.  **Install Dependencies:** Install all necessary Python libraries:
    ```bash
    pip install -r req.txt
    ```
3.  **Configure API Key:** Set your Gemini API key as an environment variable (crucial for agent functionality):
    ```bash
    GEMINI_API_KEY='YOUR_SECRET_GEMINI_KEY'
    ```
3.  **Connection File:** Verify your `db_connect.py` file contains the correct database URI for the `ai_agent` user.

### 5.3. Running the AI Agent

Execute the main Python script. The agent will initialize, and you will be prompted to enter your analytical question.

```bash
python agent.py
