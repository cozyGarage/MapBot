# MapBot

#### Hey! I'm your friendly navigator bot! Try me out, not to brag but I'm FUN!

> **🎉 Updated for 2025!** This project has been modernized with the latest Python packages and now uses spaCy for NLP processing (no more Java dependency!). Python 3.10+ is required.

## What's New in 2025?

This MapBot has been completely modernized to use current technology:

- **Modern Python Support**: Now requires Python 3.10+ (tested with 3.12)
- **Updated Dependencies**: All packages updated to 2025 versions
  - googlemaps 4.10.0 (from 2.5.1)
  - nltk 3.9.1 (from 3.4.5)
  - pandas 2.2.3 (from 0.25.1)
  - numpy 2.1.3 (from 1.16.5)
  - scikit-learn 1.5.2 (from 0.21.3)
  - mysql-connector-python 9.1.0 (from 8.0.18)
- **No More Java!**: Replaced Stanford CoreNLP with spaCy for dependency parsing
  - Faster setup - no need to download Java or Stanford CoreNLP jars
  - Better performance with modern NLP models
  - Automatic model downloads
- **Simplified Setup**: Streamlined installation process with virtual environments



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

**Step 1: Clone the repository**
```bash
git clone https://github.com/cozyGarage/MapBot.git
cd MapBot
```

**Step 2: Set up virtual environment (recommended)**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

**Step 3: Install dependencies**
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

**Step 4: Check your setup (optional but recommended)**
```bash
python check_requirements.py
```

**Step 5: Set up MySQL database**
```bash
mysql -uroot -p -hlocalhost
```
Then in MySQL:
```sql
CREATE DATABASE mapbot;
SHOW DATABASES;  -- verify creation
EXIT;
```

**Step 6: Configure the application**
- Add config.py to .gitignore: `echo "config.py" >> .gitignore`
- Remove config.py from git tracking: `git rm --cached config.py`
- Edit the `config.py` file with your values:
  - user = "root"
  - password = \<your_root_password\>
  - host = "localhost"
  - database = "mapbot"
  - key = \<your_Google_Cloud_API_key\>

**Step 7: Run MapBot!**
```bash
python init.py
```

The first run will download NLTK data automatically. After that, you're ready to chat!

------
##### Testing

You can run basic tests to verify the installation:
```bash
python test_basic.py
```

This will test:
- Module imports
- NLTK setup
- Sentence parsing with spaCy
- Feature extraction
- Classification model

------
##### How do I work?

The analysis folder contains data files for the project. The sentences.csv contains the base training dataset which is used to classify the user's input into three classes - Statement, Question, and Chat. Going through some examples would clarify the difference between statement and chat. The featuresDump.csv is the result of text pre-processing done using the code in features.py and featuresDump.py.

------
##### Want to see me in action?

Here's a [Medium article](http://bit.ly/39Y9WCq) with the some superficial explanations, there are some video links too!

