# Seven Bridges

Seven Bridges is a higher order framework, composed from the web framework technologies to build an ultra-fast, type-safe, and modern API from the Ground up on top of the Neo4j Graph Database.

## Why such a Weird Name?

_Seven Bridges_ is an homage to the fundmental, founding problems in Graph Theory called the [Seven Bridges of Königsberg](https://en.wikipedia.org/wiki/Seven_Bridges_of_Königsberg). Its a relatively easy problem to demonstrate the idea of Graph Databases. In the same way, this framework is intended to be your project's turn key solution to modeling your domain as a Graph Problem.

## Technologies Used 

* *Web Servers*:  
    * [Uvicorn (default)](https://github.com/encode/uvicorn)
    * [Hypercorn](https://gitlab.com/pgjones/hypercorn/)
    * [ManGum (AWS Lambda)](https://pypi.org/project/mangum/)
    * Use your Own (Link to docs incoming)

* GraphQL Server: [Strawberry](https://strawberry.rocks/docs)
* Rest Framework: [Fast API](https://fastapi.tiangolo.com/)

## Getting Started

Seven Bridges, while a web framework, is very CLI driven. It provides power full for code generation. Here is a short guide on how to get started with the framework using poetry. 

```
poetry new my_web_app
cd my_web_app
poetry add webversal
poetry run sb new server # or poetry run sb gen serverless if you want to boostrap an AWS Lambda Project
```

## Graph Modeling and Building your first Graph Model 

```
poetry run sb gen node Person
```

```
poetry run sb gen relationship Knows
```


```
my_web_app/
├─ model/
│  ├─ nodes/
│  │  ├─ person.py
│  ├─ relationships/
│  │  ├─ knows.py
├─ api/
│  ├─ person.py
├─ application.py

```
