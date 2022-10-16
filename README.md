# Programmierprojekt
HS Osnabrück - 5 Semester - Assessment for the module Programming Project

## Note

Implementation of the API interface only, recommendations Dataset, WEB-UI

## Task description

Netflix streams movies to its users andshared its data to provide improved
movie recommendations. You are tasked to create a recommenation system for its users.

To do this exercise, the company provides several files, such as information on the movies, and user ratings,
summing up to a total of 480189 unique users and 17770 movies.

Further details can be found here
https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data

## Project Management

The project is implemented in three sprints. Management is carried out via GitHub
https://github.com/users/ThomasWilmes/projects/1

## Access via Frontend

The frontend of this application is available via https://github.com/ThomasWilmes/Programmierprojekt_Frontend.git

## Deployment

The API is deployed via a ci/cd pipeline using github actions. With the deployment of new changes the python file is tested and later pushed to the heroku app.

Both the linting and code validity is checked before doing so.

Only after the build step is completed the deploy step begins

The two relevant enpoints are as follows:

### The list of available movies

https://backend-api-gruppe5.herokuapp.com/movies

### A recommendation based on a given movie id

https://backend-api-gruppe5.herokuapp.com/recommendation?movie_id=3

or for multiple

https://backend-api-gruppe5.herokuapp.com/recommendation?movie_id=3,5,8

## How to use

1. git clone https://github.com/ThomasWilmes/Programmierprojekt.git
1. pip3 install virtualenv
1. python -m venv env
1. .\evn\Scripts\activate
1. pip3 install -r .\requirements.txt

### Run API

1. python .\main.py

### Create Datafiles

1. Delete everything from the data folder except the testset.json
1. Download Data from Netflix prize set https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data
1. Add combined_data 1 - 4 .txt to data folder
1. Add movie_titles.csv to the data folder
1. Execute the following python code to generate the datasets (takes up to 8 mins!)

   1. python .\functions\database_operations.py init_database
   1. python .\functions\data_prep.py prepare_movies_db
   1. python .\functions\data_prep.py prepare_data
   1. python .\functions\data_prep.py create_similarity_matrix

### Run Evaluation

1. python -m data_evaluation.py
