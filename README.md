# Multi-Agent Pipeline

Demo of a **multi-agent collaboration system with long-chain reasoning**.

## Core Problem Solved
In large-scale text or data processing tasks, manual cleaning, analysis, and reporting is **time-consuming and error-prone**. This project automates the pipeline, reducing human intervention and ensuring consistent, reproducible results.

## Core Logic Flow
The pipeline consists of **four collaborating Agents**:

1. **DataFetcher** – Automatically fetches raw data (simulated in this demo).  
2. **TextCleaner** – Cleans and preprocesses text (removes stopwords, punctuation).  
3. **KeywordExtractor** – Performs long-chain reasoning to extract top keywords based on word length and order, using previous Agent outputs as input.  
4. **ReportGenerator** – Compiles the processed information into a structured report.

**Highlights:**
- Multi-Agent collaboration ensures modularity and easy extension.  
- Long-chain reasoning allows each Agent to build upon prior results.  
- Fully automated pipeline, reducing manual processing time and errors.

## How to Run

```bash
python multi_agent_pipeline.py
