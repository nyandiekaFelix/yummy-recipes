[![Build Status](https://travis-ci.org/nyandiekaFelix/yummy-recipes.svg?branch=develop)](https://travis-ci.org/nyandiekaFelix/yummy-recipes)
[![Coverage Status](https://coveralls.io/repos/github/nyandiekaFelix/yummy-recipes/badge.svg?branch=develop)](https://coveralls.io/github/nyandiekaFelix/yummy-recipes?branch=develop)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/nyandiekaFelix/yummy-recipes/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/nyandiekaFelix/yummy-recipes/?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d0438d4a4cc24ae58e734d29ec943130)](https://www.codacy.com/app/nyandiekaFelix/yummy-recipes?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=nyandiekaFelix/yummy-recipes&amp;utm_campaign=Badge_Grade)

# Yummy Recipes

Yummy Recipes enables users to write recipes, as well as view, edit or delete them.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What you need to get started:

- [Python 3](https://www.python.org/download/releases/3.0/)

- [virtualenv](https://virtualenv.pypa.io/en/stable/)

- [virtualenv-wrapper](http://virtualenvwrapper.readthedocs.io/en/latest/)

### Installing

Enter the following commands on your terminal one by one:

- *Clone this repo :*

    ```$ git clone git@github.com:nyandiekaFelix/yummy-recipes.git```

- *Move to working directory :*
    
    ``` $ cd yummy-recipes ```

- *Create your Virtual Environment :*
    
    ```$ mkvirtualenv -p python3 [environment-name] ```

- *Activate your virtual environment :*
    
    ```$ workon [environment-name] ```

- *Install project requirements :*
    
    ```$ pip install -r requirements.txt ```

- *Start the app :*
    
    ```$ python3 app.py ``` 

- *Finally navigate to ```http://localhost:8080/``` on your browser*

## Running the tests

- With Coverage Report: 
    
    ```$ nosetests --with-coverage ```

- Without Coverage: 
    
    ```$ nosetests ```

## Built With

- [Flask](http://flask.pocoo.org/)

## Authors

- [Nyandieka](https://github.com/nyandiekafelix)
