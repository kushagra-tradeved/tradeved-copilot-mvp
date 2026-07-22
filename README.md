# Tradeved Copilot MVP

This repository contains the Minimum Viable Product (MVP) for the Tradeved Copilot application[cite: 1]. It is a Python-based intelligent mentor system equipped with conversational routing, safety guardrails, and Azure integration[cite: 1]. The application uses local Excel datasets for its intelligence engine and is natively configured for serverless deployment on Vercel[cite: 1].

## Repository Structure

The core configuration and execution files included in the root of this repository are:

*   **`.gitignore`**: Specifies files and directories that should be ignored by version control[cite: 1].
*   **`main.py`**: Serves as the primary entry point for running the core application[cite: 1].
*   **`requirements.txt`**: Lists all the necessary Python dependencies required to run the project[cite: 1].
*   **`test_azure.py`**: A dedicated testing script used for validating connections and integrations with Azure services[cite: 1].
*   **`vercel.json`**: The core configuration file for deploying the application seamlessly via Vercel[cite: 1].

## Application Modules (`src/`)

The `src/` directory contains the foundational logic and programmatic components for the Tradeved mentor[cite: 1]:

*   **`src/config.py`**: Manages the environment variables, settings, and configuration parameters of the application[cite: 1].
*   **`src/data_loader.py`**: Implements the logic required to ingest, read, and parse the Excel-based intelligence datasets[cite: 1].
*   **`src/guardrails.py`**: Houses the safety guardrails and input/output validation layers to ensure secure and on-topic AI interactions[cite: 1].
*   **`src/mentor_voice.py`**: Defines the unique persona, stylistic tone, and behavioral characteristics of the Tradeved mentor[cite: 1].
*   **`src/router.py`**: Responsible for routing incoming user queries and orchestrating the operational flow between datasets and responses[cite: 1].

## Data Assets (`data/`)

The `data/` directory contains crucial Excel (`.xlsx`) datasets that drive the copilot's domain knowledge and conversational behavior[cite: 1]:

*   **`tradeved_mentor_intelligence_dataset_v4.xlsx`**: The primary knowledge base defining the mentor's core intelligence (Version 4)[cite: 1].
*   **`tradeved_mentor_longform_session_dataset_v3.xlsx`**: Structured data used to manage and guide extended, long-form mentoring sessions (Version 3)[cite: 1].
*   **`tradeved_mentor_longform_session_dataset_v3(AutoRecovered).xlsx`**: An auto-recovered backup file of the long-form session dataset[cite: 1].
*   **`tradeved_mentor_state_transition_layer_v3_1.xlsx`**: Controls the state management, transition logic, and dialog flow of the application (Version 3.1)[cite: 1].

## API Integration (`api/`)

*   **`api/index.py`**: Functions as the main serverless API endpoint[cite: 1]. It is structured specifically to handle web requests when the application is deployed to a serverless platform[cite: 1].

## Setup and Installation

1.  Ensure you have Python installed on your local environment.
2.  Clone this repository locally[cite: 1].
3.  Install the required project dependencies by running `pip install -r requirements.txt` in your terminal[cite: 1].
4.  Execute `main.py` to start the application[cite: 1]. You may also run `test_azure.py` to verify your Azure configurations[cite: 1].

## Deployment

This MVP is optimized for Vercel deployment[cite: 1]. Serverless functions are handled via the `api/index.py` routing[cite: 1], and specific deployment rules are applied automatically via the `vercel.json` file[cite: 1].
