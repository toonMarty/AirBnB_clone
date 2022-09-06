AirBnB clone Project
=====================
Description of the project
---------------------------
This project is about writing a command interpreter to manage AirBnB objects.
Each task is linked and will help you to:
    
1. put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances 
2. create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
3. create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
4. create the first abstracted storage engine of the project: File storage.
5. create all unittests to validate all our classes and storage engine

Description of the command line interpreter
------------------------------------------
This command line is limited to a specific use-case. In our case, we want to be able to manage the objects of our 
project:

1. Create a new object (ex: a new User or a new Place)
2. Retrieve an object from a file, a database etc…
3. Do operations on objects (count, compute stats, etc…)
4. Update attributes of an object
5. Destroy an object

How to start the command line interpreter
----------------------------------------
To start the command-line interpreter use the command
./console.py on a shell terminal

How to use the command line interpreter
--------------------------------------
Upon typing the ./console.py, a prompt will be displayed
The prompt will look like:

(hbnb)

The prompt then waits for the user to key in a command for example

(hbnb) help

The console then responds to the command by giving an output iff the command
has been specified in the code through parsing using the cmd module

Documented commands (type help <topic>):
________________________________________
EOF  help  quit

Above is an example of the output of the console

The console, after displaying output then displays another prompt for the user
to enter a second command. This continues(loops) until an interrupt or the 
command quit is encountered. 
Examples
--------
$ ./console.py

(hbnb) help

Documented commands (type help <topic>):
________________________________________
EOF  help  quit

(hbnb)

(hbnb)

(hbnb) quit

$
