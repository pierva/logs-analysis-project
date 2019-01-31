# Logs Analysis Project
__ __ __

This project makes use of python3 and postgres to run a simple analysis on a set of data.
The database contains articles, authors and log information of a newspaper site.
This project will answer these questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Get started
To run the project it is necessary to have postgres installed on your machine.

### Installing Postgres with Brew

In the command line run:
```sh
$ brew install postgresql
$ ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents
```
It is recommended to create two aliases:
```sh
$ alias pg_start='g_ctl -D /usr/local/var/postgres start'
$ alias pg_stop='g_ctl -D /usr/local/var/postgres stop'
```
Also, you can save these aliasas in your .bash_profile to make them availabe to every new terminal.

Further instructions on how to install postres can be found [here](https://gist.github.com/ibraheem4/ce5ccd3e4d7a65589ce84f2a3b7c23a3).

After installing postgres on your machine you can create the "postgres" and "vagrant" roles with the following command:
```sh
$ createuser -s postgres  # fixes role "postgres" does not exist
$ createuser -s vagrant  # necessary to run the sql statement if you're not using the virtual machine
```

Create the database necessary for the application (make sure the postgres server is running):
```sh
$ createdb news
```
Run the sql file to populate the newly created database (from the project directory):
```sh
$ psql news -f newsdata.sql
```

***

## Let's analyze!!!
Run app.py file with python3. The application will prompt 3 questions in the shell.
To quit the application press "q" or "quit" (Uppercase or Lowercase, it is case insensitive).
Possible answers are 1, 2, or 3.

To answer the first question the SQL statement behind the application will join the tables "articles" and "log".
This statement will make use of the slug column in the articles table to compare the valid requests with the valid articles. It will return the title and number of views (count) based on all the positive (status 200) GET requests.
The method that runs the SQL statement is:
`get_articles()`

The second question makes use of all the three tables:
 - articles
 - authors
 - log

It will return the name and views (count) per each author based on all the requests (path from the log table) compared with the aritcles table.
The method to run the second query is: `get_popular_author()`

The third question makes use only of the log table and it creates two new views:
1. total_req
2. error_req  

The first view will have the date and the total requests per each day.
The second view, instead, will have the date and the total error requests per each day.
By joining the two tables by date, we can compare the number of errors wih the total requests per each day and output the day with more than 1% of errors.
The method to run the third query is: `get_errors()`
