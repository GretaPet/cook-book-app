# CookBook App
## Resources:
Demo Video: https://we.tl/t-FhFhdDsENQ

## Brief
This is the final project for DfE Cloud Specialism. Objective of this project is to create a recipe book that keeps track of recipes. It must achieve the following:
* To create a web application that integrates with a database and demonstrates CRUD functionality.
* To utilise containers to host and deploy your application.
* To create a continuous integration (CI)/continuous deployment (CD) pipeline that will automatically test, build and deploy your application.

## Version Control
* Github and Jira
Github and Jira The project tracking software used for this project is Jira using Agile Scrum methods. I have planed out the project using user stories that are prioritized using MoSCoW methods. Each user story is divided into story points that have estimation effort measured by point system that uses fibinachi sequence. 
Jira board is integrated with the github accunt and it allows me to use smart commits to update the progress of the tasks while making pushes of the changes to GitHub repository.
A simple Risk Assesment has been written for the project

## Technologies
* Python
* Pytest
* Flask
* Docker/Docker Compose
* DockerHub
* Docker Swarm
* MySQL
* Jenkins Pipelines

## Application
The task of the project is to create a monolithic web app using Flask framework. It must demonstrates CRUD functionality and use HTML templating for the frontend to alow user to interact with the database. The backend will use SQLAlchemy to model and integrate with the database. The aplication will be hosted in a container and deployed to a Docker Swarm. 

I have chosen to create a recipe book app that keeps track of my favourite recipes and their  ingredients. I find this app to be useful and practical, also a great project to practice learning Python and it also has a vast posibility to expand functionaly.
To create this application i will use the following technologies:
Python  | Flask | Pytest | Docker | Docker Compose | DockerHub | Docker Swarm | MySQL | Jenkins Pipelines

To achieve this, I have decided to create app that must allow the user to do the following:
⦁	Load home page to see if the app is runing
⦁	Add a new dish to the database
⦁	See all the existing dishes on the database
⦁	Change the name of the dish
⦁	Delete a dish from the database
## Database
The application database has one-to-many relationship but it is posible to create this app with many-to-many relationship. To hit the MVP the application must show full CRUD functionality for at least one entity . I have created 2 spare diagrams for each type of the relationship. The first one is one-to-many and its the type that it is used for this version of the app. /Read page will store all of the dishes creating one to many relationship.
This is a possible many-to-many relationship model that could be implemented on the application. I would take an approach of creating a new page for recipes that tracks all the suitable ingreedients for each dish. 
* EDR
* SQLAlchemy
## Testing
It is important to start testing early and often. To test this application I am using pytest to write unit tests, that are run by jenkins each time the change has been made on the repository. Pytest generates coverage reports that can be viewed in Jenkins console output for the Test stage of the pipeline build.
* Pytest

![pytest][pytest]

## CI/CD
The project also requires  creating CI/CD Pipeline that automates the integration, testing and deployment of the new code. Automation server used to build the pipeline is Jenkins and it must run unit tests, build the Docker images, push Docker images to registry and deploy to a Swarm. The pipeline should be trigered everytime a new push or change is made on the github repository which is achieved by using GitHub Webhook.

CI/CD pipeline diagram

Jenkins Build Stages

Jenkins Console output for :
* Test
* Build
* Push
## Deployment
The application is deployed to Docker Swarm hosted on Azure cloud Virtual machine that works both as manager and worker nodes. For this application i am using two diferent virtual machines: development VM for Jenkins and deployment VM for Docker Swarm. They are both a part of the same virtual network, so Jenkins can automaticaly update and deploy the new version of the application to web.
* Docker Swarm
## Future Improvements
The application is working and is stable but there is a number of issues that coould be fixed or improved. 
* First, I would write more unit tests to increese the coverage of the application
* Second, I would create a new entity for the ingreedients, in order to be able to create many-to-many relationship between 2 databases. I would do that by creating a page for a Recipie that stores information of ingreedients in dish. 
* Finaly, I would like to try to improve the UI by using Bootstrap framework.



[pytest]: https://i.imgur.com/RULIu1S.jpg
