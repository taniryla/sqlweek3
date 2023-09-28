# Twitter Clone App

# Description

Miraquill is a startup that allows users to microblog poems. I am building a twitter clone using Python, MySQL4 and Flask as preparation for working as a software engineer for Miraquill.

    -The user has username, email, and password that are mandatory fields and bio, date of birthy, profile photo and background photo that are optional
    -The user can make posts that show up in a single thread timeline where the ujsers can bookmark and others can comment and retweet.

# API Reference Table For Users

| Endpoint Paths            | Methods | Parameters  |
| ------------------------- | ------- | ----------- |
| Route for all users       | GET     | ""          |
| Route for a specific user | GET     | "/<int:id>" |
| Creating a new user       | POST    | ""          |
| Deleting a user           | GET     | "/<int:id>" |

# API Reference Table For Tweets

| Endpoint Paths             | Methods | Parameters  |
| -------------------------- | ------- | ----------- |
| Route for all tweets       | GET     | ""          |
| Route for a specific tweet | GET     | "/<int:id>" |
| Creating a new tweet       | POST    | ""          |
| Deleting a tweet           | GET     | "/<int:id>" |

# ERD

![This is a snapshot of the ERD of this twitter clone app](https://imgur.com/a/RsjguHo)

# Retrospective

    -How did project's design evolve over time? I started by studying the functions of twitter and mapped all tables in an ERD. This allowed me to figure out the one-to-one, one-to-many and many-to-many relationships so that can bridge tables could be built in the case of many-to-many relationships. I next was able to build the raw SQL as documented in twitter_clones.sql Postgres database schema.
    -Did you choose to use an ORM or raw SQL? Why? For practice on raw SQL, I used the ERD and my notes on the types of foreign key references/relationships to write out the SQL code.
    - What future improvements are in store, if any? I used this project as practice for my role at Miraquill and so future improvements will be necessary.
    - Docker was not used because I had prior versions of Postgres and Django on my computer
    - Challenges included getting around Postgres issues related to the M-1 chip on my new Macbook Air.

# Technologies Used

    -A REST API built on a Python backend using the Flask Framework
    -MySQL
    -pgAdmin4 localized version
    -Insomnia
    -JWT
