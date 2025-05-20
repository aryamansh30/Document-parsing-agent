# Document Parser Agent

## Introduction
------------
The agent is a Python application that allows you to chat with multiple PDF, .docx and .txt documents. You can ask questions about the documents using natural language, and the application will provide relevant responses based on the content of the documents. This app utilizes a language model to generate accurate answers to your queries.


## Dependencies and Installation
----------------------------
To install the Agent, please follow these steps:

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

3. Obtain an API key from OpenAI and add it to the `.env` file in the project directory.
```commandline
OPENAI_API_KEY=your_secrit_api_key
```

## Usage
-----
To use the agent, follow these steps:

1. Ensure that you have installed the required dependencies and added the OpenAI API key to the `.env` file.

2. Run the `main.py` file using the Streamlit CLI. Execute the following command:
   ```
   streamlit run app.py
   ```

3. The application will launch in your default web browser, displaying the user interface.

4. Load multiple documents into the app by following the provided instructions.

5. Ask questions in natural language about the loaded PDFs using the chat interface.
