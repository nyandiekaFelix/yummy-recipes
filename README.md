[![Build Status](https://travis-ci.org/nyandiekaFelix/yummy-recipes.svg?branch=master)](https://travis-ci.org/nyandiekaFelix/yummy-recipes)
[![Coverage Status](https://coveralls.io/repos/github/nyandiekaFelix/yummy-recipes/badge.svg?branch=master)](https://coveralls.io/github/nyandiekaFelix/yummy-recipes?branch=master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/nyandiekaFelix/yummy-recipes/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/nyandiekaFelix/yummy-recipes/?branch=master)
[![Website https://yummy-recipes-c1.herokuapp.com/](https://img.shields.io/website-up-down-green-red/http/yummy-recipes-c1.herokuapp.com.svg)](https://yummy-recipes-c1.herokuapp.com/)
[![Maintainability](https://api.codeclimate.com/v1/badges/7e84426a8f8674159daf/maintainability)](https://codeclimate.com/github/nyandiekaFelix/yummy-recipes/maintainability)

# Project Title

Yummy Recipes enables users to write and share recipes, as well as view, edit or delete them.

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

[Nyandieka](https://github.com/nyandiekafelix)

## License

This project is licensed under the MIT License 