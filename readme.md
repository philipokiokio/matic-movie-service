# Matic Films Service

This is an API Service {Written in FastAPI [Python Framework]} that attends to some specifications in a document shared.

1. Get list of Films.
- Each film should contain the id, title, release date and comment count. 
- Films should be sorted in ascending order by release date.
2. Add a comment to a film
- Comment length should be limited to 500 characters
3. Get a list of comments for a film.
- Comments should be in ascending order of when they were created.
Implement automated deployment of the application to a cloud platform from the repository
- We will be leveraging the starwars open api for this. https://swapi.dev/documentation

## Deployment

finally found an alternative. 
Root Server URI: 

Documentation {OpenAPI Spec[provided out of the box with FastAPI]} URL: https://matic-films.mymixer.tech/
*  swagger: https://matic-films.mymixer.tech/docs
* redoc: https://matic-films.mymixer.tech/re-docs


## Starting the Server Locally

 The Dollar Card issue (In NGN) inhibited deployment for this project which is why the local server section is provided.

To create a virtualenv a command like
```
>$ python3 -m venv venv


```
The virtualenv can be activated via this command
```bash
 >$ source venv/bin/activate
```
There is a copy of the .env file called .example.env which provides the name of the variables used.


## Tests
This can be run locally by using the pytest command. The test case covered all edgecases and appropriate/expected responses.

```
pytest -v -s
```
