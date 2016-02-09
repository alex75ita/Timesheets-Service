## Timesheets Service

This project is an exercise for use Python 3.5 and mongoDB and develop a solution based on Hexagonal architecture and TDD (and maybe BDD).

# Project description
This is a service for registering holidays and permits of employees.

# Goals
+ Use Python 3.5
+ Use MongoDB
+ Do TDD (with Python)
+ Use Git
+ Use RabbitMQ (with Python)

This project is (at the moment) an exercise on using Python 3.5 and mongoDB and to develop a solution based on Hexagonal architecture and TDD.

# Technologies
It is a Python 3 service.
It uses mongoDB as data repository.
It uses RabbitMQ as messages broker.

I use PyCharm Community edition and I commit in the repository the necessary folders and files.
RabbitMQ server for developing is a free one (registered to Alex75) on www.cloudamqp.com

# Requirements
+ pymongo: driver for MongoDB database
+ pika: framework to manage RabbitMQ


# Todo
+ Define a structure for the mongoDB data
+ Chose how to map Python classes and mongoDB BSON documents.


# Conventions
Fuck the lower_case_with_underscore naming style: use UpperCamelCase and lowerCamelCase as in C#, Java, JavaScript, Scala.
Test files must be named as "aaa_test.py" (not "test_aaa.py") and put it in the same folder of the "aaa.py" file.
Name "ClassTest" the test file, not "TestClass".
+ RabbitMQ server  