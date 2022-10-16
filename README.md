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
2. pip3 install virtualenv
3. python -m venv env
4. .\evn\Scripts\activate
5. --> When Activation is failing: Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted --> Repeat step four
6. pip3 install -r .\requirements.txt

### Run API

1. python .\main.py

### Create Datafiles

1. Delete everything from the data folder except the testset.json
2. Download Data from Netflix prize set https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data
3. Add combined_data 1 - 4 .txt to data folder
4. Add movie_titles.csv to the data folder
5. All headings and passages are located in the Notebook Recommendation System. The data can be processed by adjusting the file paths and installing the requirements beforehand.
### Run Evaluation

1. See Notebook

### Run Frontend
1. Load index.html into the root directory of your webserver or local client
2. Kopy the style.css file in to the /%root%/cs (/cs) direcotry
3. The script ressources in the index.html header can be used or changed if necessary (Lines 8, 11, 12)
4. If you are building the API on an new server, please adjust lines 30 and 73 in the index.html accordingly
5. Good luck :-)

--> JavaScript should be enabled on the webbrowser!!!
