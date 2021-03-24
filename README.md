<br />
<p align="center">

  <h3 align="center">Cocus code challenge - by André Guilhon</h3>

  <p align="center">
    This project aims to solve the code challenge sent by Cocus Portugal
    <br />
  </p>
</p>

<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

This project was created to be the answer to Cocus Portugal Code Challenge, and make it easier to maintain if needed to change something.

### Built With

* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [ReactJS](https://reactjs.org)
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
* [Postgresql](https://www.postgresql.org/)

## Getting Started

There are some parameters that can be changed. The connection to the database is made by using envoiroment variables:
```
DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
```
Also, by default blank spaces are not considered as a character, to change that, create an environment variable `INCLUDE_BLANKS` and set it's value to True.
A random secret_key will be generated automatically once yoy start the server. If you need, you can pass it as the environment variable `SECRET_KEY`.
The file is loaded as soon as the application is lauched, and it gets cached, in order to perform better. To reload cache, just restart the server.
If you run the project locally, you might need to set the environment variable `RUNNING_PORT` to the port you run your Django instance. This is needed to get the get_quote command working.
There are two ways to get started:
One is to use Docker and Docker-compose. This is the easier one;
The second one is to use it locally and build the whole environment.

### Prerequisites (Running in docker)

* Docker
* Docker-compose

### Installation

1. Clone the repo
2. From the cloned root folder, simply run `docker-compose up -d`. The `-d` switch is for detaching it from your console and let you use it again.

It will run all the needed parts, and start the server at your localhost, on port 8020. You can acesses it by browsing to http://localhost:8020


## Usage

To get a random line of a local "quotes" file (available in filereader/reader/quotes.txt), simply make a GET request to http://localhost:8020/reader. It will return to you a random quote, encapsuled in JSON, containing the contents of the line, as well as the line number of the file. If you need it encapsuled in XML, add a "Accept" header to your request, whcih the value is "application/xml". 

You can also populate your Database with some lines from the file, as well as the most common character in the line and the line number. For that, still in the root folder, run the command `docker-compose exec web python filereader/manage.py get_quote`. This will run `python filereader/manager.py get_quote` command inside the docker container. It will tell you if it added a new line to the Database, or if the line already existed (in that case, it won't change the contents for that line, nor duplicate the line). Additionally, you can add a `--number_of_quotes=10` to the end of the command. It will try to fetch and insert 10 (or whatever number you pass to it) to the database at once.

Finally, if you want to show the quotes in the database, 5 at a time, you may access http://localhost:8020/. It will show you 5 random quotes, including the most frequent character. Also, it will tell you which is the character that is the most frequent among the most frequent for each quote. 
You'll also find a button, that let's you fetch another quote from the database, and put it right bellow the last one you had. You can do it as many times as you need. 

## Contact

André Guilhon - andre.guilhon@gmail.com / andre@guilhon.dev.br

Project Link: [https://github.com/andreguilhon/cocus_codechallenge](https://github.com/andreguilhon/cocus_codechallenge)

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->