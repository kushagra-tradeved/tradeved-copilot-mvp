# Tradeved Copilot MVP

This repository contains the Minimum Viable Product (MVP) for the Tradeved Copilot application. It is a Python-based intelligent mentor system equipped with conversational routing, safety guardrails, and Azure integration. The application uses local Excel datasets for its intelligence engine and is natively configured for serverless deployment on Vercel.

## Repository Structure

The core configuration and execution files included in the root of this repository are:

*   **`.gitignore`**: Specifies files and directories that should be ignored by version control.
*   **`main.py`**: Serves as the primary entry point for running the core application.
*   **`requirements.txt`**: Lists all the necessary Python dependencies required to run the project.
*   **`test_azure.py`**: A dedicated testing script used for validating connections and integrations with Azure services.
*   **`vercel.json`**: The core configuration file for deploying the application seamlessly via Vercel.

## Application Modules (`src/`)

The `src/` directory contains the foundational logic and programmatic components for the Tradeved mentor:

*   **`src/config.py`**: Manages the environment variables, settings, and configuration parameters of the application.
*   **`src/data_loader.py`**: Implements the logic required to ingest, read, and parse the Excel-based intelligence datasets.
*   **`src/guardrails.py`**: Houses the safety guardrails and input/output validation layers to ensure secure and on-topic AI interactions.
*   **`src/mentor_voice.py`**: Defines the unique persona, stylistic tone, and behavioral characteristics of the Tradeved mentor.
*   **`src/router.py`**: Responsible for routing incoming user queries and orchestrating the operational flow between datasets and responses.

## Data Assets (`data/`)

The `data/` directory contains crucial Excel (`.xlsx`) datasets that drive the copilot's domain knowledge and conversational behavior:

*   **`tradeved_mentor_intelligence_dataset_v4.xlsx`**: The primary knowledge base defining the mentor's core intelligence (Version 4).
*   **`tradeved_mentor_longform_session_dataset_v3.xlsx`**: Structured data used to manage and guide extended, long-form mentoring sessions (Version 3).
*   **`tradeved_mentor_longform_session_dataset_v3(AutoRecovered).xlsx`**: An auto-recovered backup file of the long-form session dataset.
*   **`tradeved_mentor_state_transition_layer_v3_1.xlsx`**: Controls the state management, transition logic, and dialog flow of the application (Version 3.1).

## API Integration (`api/`)

*   **`api/index.py`**: Functions as the main serverless API endpoint. It is structured specifically to handle web requests when the application is deployed to a serverless platform.

## Setup and Installation

1.  Ensure you have Python installed on your local environment.
2.  Clone this repository locally.
3.  Install the required project dependencies by running `pip install -r requirements.txt` in your terminal.
4.  Execute `main.py` to start the application. You may also run `test_azure.py` to verify your Azure configurations.

## Deployment

This MVP is optimized for Vercel deployment. Serverless functions are handled via the `api/index.py` routing, and specific deployment rules are applied automatically via the `vercel.json` file.
