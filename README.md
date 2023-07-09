# Calyx-Final-Project


Virtual env
-------------


Create venv:

`py -m venv venv`


With the virtual environment activated, download the requirements:

`pip install -r requirements.txt`


Execute
-------------

Download csv by bot:

`python bot.py`


Create the database:

`python main.py`


Processing the dataset and importing data into the database:

`python processing.py`


Run the api:

`uvicorn main:app --reload`
