# Custom Database Assistant
===========================

## Overview
This project is a custom database assistant that utilizes the open-source Google PaLM LLM to connect with your database. The assistant requires the following information to connect with your database:

* Host
* Port
* User
* Password
* Database name

## Installation
### Prerequisites

* Python 3.10 or 3.11
* Google PaLM API key (or OpenAI API key if preferred)

### Instructions

1. Clone the repository:
    ```sh
    git clone https://github.com/NandaKishoreYadav/Custom-Database-Assistant.git
    ```
2. Obtain your Google PaLM API key for free from [Google AI Studio](https://aistudio.google.com/app/apikey) and paste it in the `.env` file. If you prefer to use OpenAI, obtain an API key from OpenAI and use it.

3. Open a command prompt from the project directory and create a new virtual environment:
    ```sh
    python -m venv myenv
    ```
4. Activate your environment:
    - On Windows:
        ```sh
        myenv\Scripts\activate
        ```
    - On Linux:
        ```sh
        source myenv/bin/activate
        ```
5. Install the necessary dependencies:
    ```sh
    pip install -r requirements.txt
    ```
6. Run the application:
    ```sh
    streamlit run app.py
    ```

## Usage
To use the custom database assistant, simply run the application and follow the prompts to connect with your database.

### Note

Sometimes the prompts may give errors due to the use of the open-source model. If you encounter such issues, change the prompt and try again; it should work fine.


## Contact

If you have any questions or feedback, please feel free to reach out.

Thank you for using Custom DataBase Assistant! 😊
