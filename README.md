## Prerequisites
PLEASE BE SURE TO INSTALL AND USE PYTHON 3.6.7
### Install Python

1. Install Python 3.6.7 using PyEnv:
    * `$ brew install pyenv`
    * `$ pyenv install 3.6.7` 
    * `$ pyenv global 3.6.7`
    * `$ echo eval "$(pyenv init -)" >> ~/.bash_profile` 
        * `$ source ~/.bash_profile` 
    * `$ pip install --upgrade pip`

2. Check Python and Pip versions:
    * `$ python --version`
        * returns `python 3.6.7`
    * `$ pip --version`
        * returns `pip 18.1 (or greater)`


Set Up Tests
============

1. clone repo
    * `git clone https://github.com/NykoriakArtem/project.git`
2. From root of repo create the virtual environment
    * `python -m venv venv`
3. Activate / enter the virtual environment
    * `source venv/bin/activate`
4. Upgrade pip within virtual environment
    * `pip install -U pip`
5. Download the projects requirements inside the virtual env
    * `pip install -r requirements.txt`

Set Up Docker
=============

Make sure that you have [docker for mac](https://docs.docker.com/docker-for-mac/install/) installed on your machine and that you are logged in. 

1. `docker-compose up -d`
2. Go to http://localhost:4444/grid/admin/live
    * Watch test run through VNC here
3. Go to http://localhost:4444/dashboard/#
    * Watch stored historical test runs

Run Tests
=========

### Prerequisites
This repo utilizes [dotenv](https://pypi.org/project/python-dotenv/) which is how I store username and password so they are not stored in github.
None of the tests will be able to run without a local version of `.env` file. Create a `.env` file on your local with fields:
* ADMIN_USER_EMAIL=username/email
* ADMIN_USER_PASSWORD=password
* USER_AUTH=user_authorization
* USER_API_KEY=user_api_key

##### Precursor
These tests utilize `pytest.ini` to store pytest commands that are always going to run with these tests. The commands are:

1. [--reruns 2](https://pypi.org/project/pytest-rerunfailures/)
    * This allows the tests to run a total of 3 times before a failure occurs. 
        * Set `--reruns 0` if you want the test to run once during debugging.
            * This can be done in cli `pytest --reruns 0 tests/`, or changing the ini file
2. [--workers auto --tests-per-worker auto](https://pypi.org/project/pytest-parallel/)
    * This sets up the tests to run in parallel based on your computers cores'.
3. [--html=report.html --self-contained-html](https://pypi.org/project/pytest-html/)    
    * This will create or overwrite a report with the name `report.html` on every test run.


### Running the Tests
 
The tests are setup to run using PyTest and can be run through CLI within root of the repo.

    
To run a single test the command would be :

   * `pytest tests/login_test.py`
    