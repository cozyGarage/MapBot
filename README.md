# MapBot

#### Hey! I'm your friendly navigator bot! Try me out, not to brag but I'm FUN!

> **🎉 Updated for 2025!** This project has been modernized with the latest Python packages and now uses spaCy for NLP processing (no more Java dependency!). Python 3.10+ is required.



##### What I do?

I aim to give users a new way to interact with Google Maps through engaging text-based conversational interfaces. 

##### How old am I?

I'm only a baby bot right now, I need you to feed me with logic, data and inspiration.

##### What is the motivation behind building me?

The primary motivation of the developers of MapBot is to provide a playground to tech enthusiasts, both beginners and advanced to try algorithms, approaches and ideas while contributing to a real-life project. 

##### What I aspire to be one day?

- I want to help users in the most comprehensive way.
- I want to give 'geeks' a platform to try out all things 'cool'.

------

##### Are you here for GSSoC 2020?

Check out all related information [here](GSSoC.md)

------

##### What are some pre-requisites?

-  Python 3.10 or higher
  - Verify installation with `python --version` or `python3 --version`
-  MySQL 
  - Install the community version of MySQL from the [official MySQL documentation page](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/). 
  - Create root user credentials during installation.
  - Verify the installation, running the command  `mysql -uroot -p -hlocalhost` should open the MySQL monitor. (Enter the root password when prompted)  

##### How to set me up?
- Clone the repository
- Create the **mapbot** database in MySQL
  -  `mysql -uroot -p -hlocalhost` 
  - Enter root password when prompted
  - `create database mapbot;`
  - Verify creation of the database `show databases;`
- It is recommended to set this project up in a virtual environment:
  ```bash
  # Create virtual environment
  python -m venv venv
  
  # Activate virtual environment
  # On Linux/Mac:
  source venv/bin/activate
  # On Windows:
  venv\Scripts\activate
  ```
- Install dependencies from `requirements.txt` file:
  ```bash
  pip install -r requirements.txt
  ```
- The spaCy English language model will be automatically downloaded on first run
- Add config.py file to .gitignore to avoid pushing changes made to config
- Run `git rm --cached config.py`
- Edit the config.py file with the corresponding values:
  - user = "root"
  - password = <your_root_password>
  - host = "localhost"
  - database = "mapbot"
  - key = <your_Google_Cloud_API_key>
- You're all set up, run the `init.py` file: `python init.py`

------
##### How do I work?

The analysis folder contains data files for the project. The sentences.csv contains the base training dataset which is used to classify the user's input into three classes - Statement, Question, and Chat. Going through some examples would clarify the difference between statement and chat. The featuresDump.csv is the result of text pre-processing done using the code in features.py and featuresDump.py.

------
##### Want to see me in action?

Here's a [Medium article](http://bit.ly/39Y9WCq) with the some superficial explanations, there are some video links too!

