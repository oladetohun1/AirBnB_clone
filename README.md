# hBnB (AirBnB CLone Project)
![HolBnB clone](./hBnB.png)

This is a clone of the popular vacation rental platform AirBnB. The project provides a command-line interface for managing users, locations, and properties, and includes a simple file-based storage engine.

## Getting Started

 
**What’s a command interpreter?**

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to

be able to manage the objects of our project:

  

- Create a new object (ex: a new User or a new Place)

- Retrieve an object from a file, a database etc…

- Do operations on objects (count, compute stats, etc…)

- Update attributes of an object

- Destroy an object

The command interpreter provides a simple way to interact with the AirBnB clone. It includes a set of commands for managing users, locations, and properties, as well as some utility commands for listing available commands and exiting the application.

## Starting the Command Interpreter
To start the command interpreter, navigate to the project directory and run ````console.py```` using Python:

````
$ ./console.py
````

## Execution

  
Your shell should work like this in interactive mode:

  
````
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$
````

But also in non-interactive mode: (like the Shell project in C)

````
$ echo "help" | ./console.py

(hbnb)

Documented commands (type help <topic>):
========================================

EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

  
Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb)
$

````

## Using the Command Interpreter

**Launching the console**

````
$ ./console.py
(hbnb) 

````


**Creating a new object**
````
(hbnb) create
** class name missing **
(hbnb) create User
670265eb-5982-489e-8b92-2dff054f0776
````

**Show an object**

````
(hbnb) show User
** instance id missing **
(hbnb) show User 670265eb-5982-489e-8b92-2dff054f0776
[User] (670265eb-5982-489e-8b92-2dff054f0776) {'created_at': datetime.datetime(2020, 2, 19, 18, 8, 58, 458246), 'id': '670265eb-5982-489e-8b92-2dff054f0776', 'updated_at': datetime.datetime(2020, 2, 19, 18, 8, 58, 458261)}

````

**Update an object**

````
(hbnb) all
["[User] (70f71c16-962b-48ad-9df8-9203fe23d612) {'created_at': datetime.datetime(2020, 2, 19, 18, 11, 32, 341144), 'id': '70f71c16-962b-48ad-9df8-9203fe23d612', 'updated_at': datetime.datetime(2020, 2, 19, 18, 11, 32, 341161)}"]
(hbnb) updatei
** class name missing **
(hbnb) update User
** instance id missing **
(hbnb) update User 70f71c16-962b-48ad-9df8-9203fe23d612
** attribute name missing **
(hbnb) update User 70f71c16-962b-48ad-9df8-9203fe23d612  Age "20"
(hbnb) all
["[User] (70f71c16-962b-48ad-9df8-9203fe23d612) {'Age': 20, 'created_at': datetime.datetime(2020, 2, 19, 18, 11, 32, 341144), 'id': '70f71c16-962b-48ad-9df8-9203fe23d612', 'updated_at': datetime.datetime(2020, 2, 19, 18, 13, 9, 937933)}"]
(hbnb)

````
**Destroy an object**

````
(hbnb) destroy
** class name missing **
(hbnb) destroy User
** instance id missing **
(hbnb) destroy User 670265eb-5982-489e-8b92-2dff054f0776
(hbnb)

````

## Examples with data

### Create a new user
````
(hbnb) create User email="example@example.com" password="password" first_name="John" last_name="Doe"
````
### List all users
````
(hbnb) all User
````

### Create a new state
````
(hbnb) create State name="California"
````

### Create a new city
````
(hbnb) create City state_id="STATE_ID" name="San Francisco"
````

### Create a new property
````
(hbnb) create Place city_id="CITY_ID" user_id="USER_ID" name="Cozy Cottage" description="A charming and cozy cottage in the heart of San Francisco" number_rooms=2 number_bathrooms=1 max_guest=4 price_by_night=100 latitude=37.7749 longitude=-122.4194 amenity_ids="[1, 2, 3]"
````
#### List all properties
````
(hbnb) all Place
````

---

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

---
## Authors

[oladetohun1](https://www.github.com/oladetohun1)


[jefferyson](https://www.github.com/jefferyson)
