# Online Judge System

Written in [Python](https://www.python.org/) and powered by [Django](https://www.djangoproject.com/), this system aims to conduct programmming contests. 
It can run code, and test them with pre-constructed data. Submitted code will be run with a time limit restriction. 
The output of the code will be captured by the system, and compared with the standard output. The system returns the following results-
- AC : Accepted
- WA : Wrong Answer
- TLE : Time Limit Exceeded
- RTE : Run Time Error

## Deploying System
### Installing Dependencies
> This is taken from [Django](https://www.djangoproject.com/)'s official documentation and modified according to the installation requirement of the project. You can check out Django's guide to installation [here](https://docs.djangoproject.com/en/1.11/topics/install/).

#### Install Python
Being a Python Web framework, Django requires Python. See [What Python version can I use with Django?](https://docs.djangoproject.com/en/1.11/faq/install/#faq-python-version-support) for details. Get the latest version of Python at [https://www.python.org/downloads/](https://www.python.org/downloads/) or with your operating system’s package manager.

#### Installing Django's official release with pip
1. Install [pip](https://pip.pypa.io/en/stable/). The easiest is to use the [standalone pip installer](https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py). If your distribution already has pip installed, you might need to update it if it’s outdated. If it’s outdated, you’ll know because installation won’t work.. 
2. Take a look at [virtualenv](https://virtualenv.pypa.io/) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/). These tools provide isolated Python environments, which are more practical than installing packages systemwide. They also allow installing packages without administrator privileges. See [how to create a virtualenv on Python 3](https://docs.djangoproject.com/en/1.11/intro/contributing/).
3. After you’ve created and activated a virtual environment, enter the command `pip install Django~=1.11` at the shell prompt.

### Running System
#### Clonning repository
```
git clone https://github.com/minusv23/Online-Judge-System-.git
```
> Complete the following steps in the directory containing `manage.py`.
#### Migrating database
```
python manage.py migrate
```
#### Making admin credentials for the System
```
python manage.py createsuperuser
```
#### Running server
```
python manage.py runserver
```
***Congratulations!*** System is up and running!
> **Note:** The system currently supports only *Python* as an allowed language to participate in the contest.
