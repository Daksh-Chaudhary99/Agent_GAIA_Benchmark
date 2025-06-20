# Multimodal AI Agent for the GAIA Benchmark

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![LlamaIndex](https://img.shields.io/badge/Framework-LlamaIndex-blueviolet.svg)
![Model](https://img.shields.io/badge/LLM-Qwen/Gemma-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/DakshC/Agent_GAIA_Benchmark)

## Project Overview

This repository contains the source code for a sophisticated, multimodal AI agent designed to solve complex, real-world reasoning tasks from the **GAIA (General AI Assistants) benchmark**. This project demonstrates a deep, practical application of modern agentic AI principles, including multi-tool usage, advanced prompt engineering, and interaction with external APIs and local files.

The agent was developed iteratively to tackle a challenging subset of the GAIA Level 1 questions, which are designed to be simple for humans but remarkably difficult for even state-of-the-art AI systems.

The final agent successfully achieved a score of **35% (7/20 correct answers)**, significantly outperforming the original GPT-4 with plugins baseline of ~15% cited in the GAIA paper.

---

## The Challenge: The GAIA Benchmark

To understand the complexity of this project, it's essential to understand the benchmark it was designed for.

> **What is GAIA?**
>
> GAIA is a benchmark designed to evaluate AI assistants on real-world tasks that require a combination of core capabilities - such as reasoning, multimodal understanding, web Browse, and proficient tool use. It was introduced in the paper ”GAIA: A Benchmark for General AI Assistants”.
>
> **GAIA’s Core Principles:**
>
> -   **🔍 Real-world difficulty:** Tasks require multi-step reasoning, multimodal understanding, and tool interaction.
> -   **🧾 Human interpretability:** Despite their difficulty for AI, tasks remain conceptually simple and easy to follow for humans.
> -   **🛡️ Non-gameability:** Correct answers demand full task execution, making brute-forcing ineffective.
> -   **🧰 Simplicity of evaluation:** Answers are concise, factual, and unambiguous—ideal for benchmarking.

---

## Agent Capabilities & Key Features

The final agent is a robust system equipped with a versatile toolbox, enabling it to handle a wide variety of tasks:

* **Advanced Web Research:** Utilizes the **Tavily Search API** to perform AI-native web searches, scraping and synthesizing information from multiple sources to answer complex research questions.
* **Multimodal Vision:** Capable of analyzing images to answer questions about their content (e.g., solving a chess puzzle from a board image). This is achieved through a custom-built tool integrating a powerful Vision-Language Model (VLM).
* **Data Analysis & Spreadsheet Interaction:** Can process and answer questions about structured data in Excel (`.xlsx`) files by dynamically generating and executing **Pandas** code queries.
* **File System Interaction:** Can download required files (images, documents, etc.) from a remote API and use them in its local environment, forming the basis for its multimodal capabilities.
* **Safe Mathematical Calculation:** Equipped with a secure calculator tool (using `numexpr`) to perform precise mathematical calculations, avoiding the risks of standard `eval()` methods.
* **Sophisticated Reasoning & Planning:** Built on a **ReAct (Reasoning and Acting)** framework, allowing the agent to think step-by-step, choose the correct tool, learn from its observations, and recover from errors.
* **Advanced Prompt Engineering:** Utilizes a custom system prompt with **few-shot examples** to strictly control the agent's behavior and ensure its final output conforms to the exact match requirements of the benchmark.

---

## Technical Architecture & Stack

This project leverages a modern stack of AI and Python technologies:

* **Core Framework:** **LlamaIndex** (`ReActAgent`)
* **LLM "Brain":** **Qwen** and **Gemma** models served via the **NebiusAI** API (OpenAI-compatible).
* **Tooling & Integrations:**
    * **Web Research:** `llama-index-tools-tavily-research`
    * **Data Analysis:** `llama-index-experimental` (`PandasQueryEngine`)
    * **Vision:** Custom tool built with the `openai` library to interface with NebiusAI's vision models.
    * **Calculation:** Custom `numexpr`-based tool for safe math evaluation.
* **Environment:** Python, Gradio (for the interactive UI).

### Example Agent Workflow (Data Analysis Task)

To solve a question about an Excel file, the agent demonstrates its multi-step reasoning:

1.  **Thought:** "The question mentions an attached Excel file. I must download it first."
2.  **Action:** Calls the `file_downloader` tool with the correct `task_id` and `file_name`.
3.  **Observation:** Receives the local path to the downloaded file (e.g., `downloads/sales_data.xlsx`).
4.  **Thought:** "Now that I have the file, I need to analyze its contents to calculate the total sales. I will use the `spreadsheet_analyzer` tool."
5.  **Action:** Calls the `spreadsheet_analyzer` tool, passing it both the `file_path` and the specific question about the data.
6.  **Observation:** The tool's `PandasQueryEngine` generates and executes Pandas code, returning the final numerical result (e.g., `897.06`).
7.  **Thought:** "I have the final calculated number. I can now provide the final answer."
8.  **FINAL ANSWER:** `897.06`

---

## Results & Future Work

* **Current Score:** **35% (7/20)** on the GAIA Level 1 validation set.
* **Key Achievement:** Successfully engineered a system that more than doubles the performance of the original GPT-4 + plugins baseline (~15%).

This project serves as a strong foundation. Future work to further improve the score includes:

* **Implementing an Audio Tool:** Building the final tool for speech-to-text transcription (e.g., using a Whisper API) to solve audio-based questions. This is the next planned step and is projected to increase the score to **45%**.
* **Advanced Error Analysis:** Analyzing the remaining incorrect answers to identify and fix subtle reasoning flaws or prompt misinterpretations.
* **Improving Prompt Robustness:** Adding more complex few-shot examples to handle edge cases and logical puzzles more effectively.

---

## Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone [your-repo-url]
    cd [your-repo-name]
    ```
2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set Environment Variables:**
    Create a `.env` file or set the following environment variables with your API keys:
    ```
    NEBIUS_API_KEY="your_nebius_api_key"
    TAVILY_API_KEY="your_tavily_api_key"
    ```
5.  **Run the application:**
    ```bash
    python app.py
    ```
