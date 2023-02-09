# AirBnB Clone [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/sekaycee/AirBnB_clone/blob/master/LICENSE)
![HBnB](./hbnb.png)

## Synopsis
This is the initial phase of a four-phase project. Aiming to create a basic clone of the [AirBnB](https://airbnb.com) web app. In this initial phase, a basic console was created using the Cmd Python module. To manage the objects of the whole project. It's able to implement the methods create, show, update, all, and destroy, to the existing classes and subclasses.

## Technologies
* Scripts are written in Python3
* Tested on Ubuntu and Windows

## Files
This repository contains the following files:

|   **File**   |   **Description**   |
| -------------- | --------------------- |
|[AUTHORS](./AUTHORS) | Contain info about authors of the project |
|[base_model.py](./models/base_model.py) | Define BaseModel class (parent class), and methods |
|[user.py](./models/user.py) | Define subclass User |
|[amenity.py](./models/amenity.py) | Define subclass Amenity |
|[city.py](./models/city.py)| Define subclass City |
|[place.py](./models/place.py)| Define subclass Place |
|[review.py](./models/review.py) | Define subclass Review |
|[state.py](./models/state.py) | Define subclass State |
|[file_storage.py](./models/engine/file_storage.py) | Create new instance of class, serializes and deserializes data |
|[console.py](./console.py) | create and retrieve object from file, do operations on objects, update attributes of object and destroy object |
|[test_base_model.py](./tests/test_models/test_base_model.py) | unittests for base_model |
|[test_user.py](./tests/test_models/test_user.py) | unittests for user |
|[test_amenity.py](./tests/test_models/test_amenity.py) | unittests for amenity |
|[test_city.py](./tests/test_models/test_city.py) | unittests for city |
|[test_place.py](./tests/test_models/test_place.py) | unittests for place |
|[test_review.py](./tests/test_models/test_review.py) | unittests for review |
|[test_state.py](./tests/test_models/test_state.py) | unittests for state |
|[test_file_storage.py](./tests/test_models/test_engine/test_file_storage.py) | unittests for file_storage |
|[test_console.py](./tests/test_console.py) | unittests for console |

## Features
### Command Interpreter
#### Description
The Command Interpreter is used to manage the whole application's functionality from the command line, such as:
+ Create a new object.
+ Retrieve an object from a file, database, etc.
+ Execute operation on objects. e.g. Count, compute statistics, etc.
+ Update object's attributes.
+ Destroy an object.

#### Installation
Fork and clone the repository using:

```$ git clone git@github.com:<username>/AirBnB_clone.git```

#### Usage
Launch the console application in interactive mode by running:

```$ ./console.py ```

or to use the non-interactive mode run:

```$ echo "your-command-goes-here" | ./console.py ```

#### Commands
| Commands | Description | Usage |
| -------- | ----------- | ----- |
| **help** or **?**| Displays the documented commands. | **help** |
| **quit**     | Exits the program. | **quit** |
| **EOF**      | Ends the program. Used when files are passed into the program. | N/A |
| **create**  | Creates a new instance of the \<class_name\>. Creates a Json file with the object representation. and prints the id of created object. | **create** \<class_name\> |
| **show**    | Prints the string representation of an instance based on the class name and id. | **show** \<class_name class_id\> |
| **destroy** | Deletes and instance base on the class name and id. | **destroy** \<class_name class_id\> |
| **all** | Prints all string representation of all instances based or not on the class name | **all** or **all** \<class_name class_id\> |
| **update** | Updates an instance based on the class name and id by adding or updating attribute | **update** \<class_name class_id key value\> |

#### Examples
##### No 1
```
~/alx/AirBnB_clone $ ./console.py
(hbnb) create User
c2b0b1e2-4f60-4a5b-a8fa-901fa4ecee2c
(hbnb) all User
["[User] (c2b0b1e2-4f60-4a5b-a8fa-901fa4ecee2c) {'id': 'c2b0b1e2-4f60-4a5b-a8fa-901fa4ecee2c', 'created_at': datetime.datetime(2023, 2, 7, 14, 56, 6, 411963), 'updated_at': datetime.datetime(2023, 2, 7, 14, 56, 6, 412151)}"]
(hbnb) show User
** instance id missing **
(hbnb) show User c2b0b1e2-4f60-4a5b-a8fa-901fa4ecee2c
[User] (c2b0b1e2-4f60-4a5b-a8fa-901fa4ecee2c) {'id': 'c2b0b1e2-4f60-4a5b-a8fa-901fa4ecee2c', 'created_at': datetime.datetime(2023, 2, 7, 14, 56, 6, 411963), 'updated_at': datetime.datetime(2023, 2, 7, 14, 56, 6, 412151)}
(hbnb) update User c2b0b1e2-4f60-4a5b-a8fa-901fa4ecee2c name Kaycee
(hbnb) show User c2b0b1e2-4f60-4a5b-a8fa-901fa4ecee2c
[User] (c2b0b1e2-4f60-4a5b-a8fa-901fa4ecee2c) {'id': 'c2b0b1e2-4f60-4a5b-a8fa-901fa4ecee2c', 'created_at': datetime.datetime(2023, 2, 7, 14, 56, 6, 411963), 'updated_at': datetime.datetime(2023, 2, 7, 14, 57, 45, 275479), 'name': 'Kaycee'}
(hbnb) destroy User c2b0b1e2-4f60-4a5b-a8fa-901fa4ecee2c
(hbnb) all
[]
```
##### No 2
```
➜  AirBnB_clone git:(feature) ✗ ./console.py
(hbnb) User.create
*** Unknown syntax: User.create
(hbnb) User.create()
e6ee5344-04ef-454d-84e4-ba6fc610f1b4
(hbnb) User.all()
["[User] (e6ee5344-04ef-454d-84e4-ba6fc610f1b4) {'id': 'e6ee5344-04ef-454d-84e4-ba6fc610f1b4', 'updated_at': datetime.datetime(2023, 2, 10, 17, 14, 1, 963404), 'created_at': datetime.datetime(2023, 2, 10, 17, 14, 1, 963373)}"]
(hbnb) User.show()
** instance id missing **
(hbnb) User.show(e6ee5344-04ef-454d-84e4-ba6fc610f1b4)
[User] (e6ee5344-04ef-454d-84e4-ba6fc610f1b4) {'id': 'e6ee5344-04ef-454d-84e4-ba6fc610f1b4', 'updated_at': datetime.datetime(2023, 2, 10, 17, 14, 1, 963404), 'created_at': datetime.datetime(2023, 2, 10, 17, 14, 1, 963373)}
(hbnb) User.update("e6ee5344-04ef-454d-84e4-ba6fc610f1b4", "name", "Betty")
['User', '"e6ee5344-04ef-454d-84e4-ba6fc610f1b4"', '"name"', '"Betty"']
(hbnb) User.all()
['[User] (e6ee5344-04ef-454d-84e4-ba6fc610f1b4) {\'"name"\': \'"Betty"\', \'id\': \'e6ee5344-04ef-454d-84e4-ba6fc610f1b4\', \'updated_at\': datetime.datetime(2023, 2, 10, 17, 14, 1, 963404), \'created_at\': datetime.datetime(2023, 2, 10, 17, 14, 1, 963373)}']
(hbnb) User.destroy(e6ee5344-04ef-454d-84e4-ba6fc610f1b4)
(hbnb) User.all()
[]
(hbnb) quit
➜  AirBnB_clone git:(feature) ✗
```

##### No 3
```
~/alx/AirBnB_clone $ ./console.py
(hbnb) create User
44e2b0b4-c894-4bed-9b63-57ea8d16a5d5
(hbnb) User.create()
68397696-0346-4baf-a6d7-19bb09791751
(hbnb) all
["[User] (44e2b0b4-c894-4bed-9b63-57ea8d16a5d5) {'id': '44e2b0b4-c894-4bed-9b63-57ea8d16a5d5', 'created_at': datetime.datetime(2023, 2, 9, 12, 56, 24, 237836), 'updated_at': datetime.datetime(2023, 2, 9, 12, 56, 24, 238250)}", "[User] (68397696-0346-4baf-a6d7-19bb09791751) {'id': '68397696-0346-4baf-a6d7-19bb09791751', 'created_at': datetime.datetime(2023, 2, 9, 12, 56, 32, 749147), 'updated_at': datetime.datetime(2023, 2, 9, 12, 56, 32, 749378)}"]
(hbnb) User.update('44e2b0b4-c894-4bed-9b63-57ea8d16a5d5', {'first_name': 'Caleb', 'age': 27})
(hbnb) update User 68397696-0346-4baf-a6d7-19bb09791751 {'first_name': 'Joshua', 'age': 20}
(hbnb) all
["[User] (44e2b0b4-c894-4bed-9b63-57ea8d16a5d5) {'id': '44e2b0b4-c894-4bed-9b63-57ea8d16a5d5', 'created_at': datetime.datetime(2023, 2, 9, 12, 56, 24, 237836), 'updated_at': datetime.datetime(2023, 2, 9, 12, 59, 25, 552020), 'first_name': 'Caleb', 'age': 27}", "[User] (68397696-0346-4baf-a6d7-19bb09791751) {'id': '68397696-0346-4baf-a6d7-19bb09791751', 'created_at': datetime.datetime(2023, 2, 9, 12, 56, 32, 749147), 'updated_at': datetime.datetime(2023, 2, 9, 13, 0, 53, 107105), 'first_name': 'Joshua', 'age': 20}"]
(hbnb) User.update('44e2b0b4-c894-4bed-9b63-57ea8d16a5d5', {'first_name': 'Praise', 'age': 18})
(hbnb) all
["[User] (44e2b0b4-c894-4bed-9b63-57ea8d16a5d5) {'id': '44e2b0b4-c894-4bed-9b63-57ea8d16a5d5', 'created_at': datetime.datetime(2023, 2, 9, 12, 56, 24, 237836), 'updated_at': datetime.datetime(2023, 2, 9, 13, 2, 9, 955866), 'first_name': 'Praise', 'age': 18}", "[User] (68397696-0346-4baf-a6d7-19bb09791751) {'id': '68397696-0346-4baf-a6d7-19bb09791751', 'created_at': datetime.datetime(2023, 2, 9, 12, 56, 32, 749147), 'updated_at': datetime.datetime(2023, 2, 9, 13, 0, 53, 107105), 'first_name': 'Joshua', 'age': 20}"]
(hbnb) quit
~/alx/AirBnB_clone $
```
## Tests
If you wish to run all the tests for this application,  the tests are located in the **tests/** directory and you can execute all of them by running:

```$ python3 -m unittest discover tests ```

from the root directory.
