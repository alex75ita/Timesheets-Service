## Timesheets Service

This project is an exercise for use Python 3.5 and mongoDB and develop a solution based on Hexagonal architecture and TDD (and maybe BDD).

# Goals
This is a service for registering holidays and permits of employees.

This project is (at the moment) an exercise for use Python 3.5 and mongoDB and develop a solution based on Hexagonal architecture and TDD.

# Technologies
It is a Python 3 service.
It uses mongoDB as data repository.
It uses RabbitMQ as messages broker.

I use PyCharm Community edition and I commit in the repository the necessary folders and files.

# Requirements
+ pymongo: driver for MongoDB database
+ pika: framework to manage RabbitMQ


# Todo

+ Define a structure for the mongoDB data
+ Chose how to map Python classes and mongoDB BSON documents.


# Naming convention
Fuck the lower_case_with_underscore naming style: use UpperCamelCase and lowerCamelCase.
Name test file as "aaa_test.py" (not "test_aaa.py") and put it in the same folder of the "aaa.py" file.
Name "ClassTest" the test file, not "TestClass".
 