# School python project 2

This is group 20's second solution to the python exercises. This project is an application that allows you to search for a movie in the omdb movie database. Once you search the name of the movie, the application categorizes the movies from the search results into the genres each movie belongs to. The application also gives you the option to view a pie chart of the movie results.

# Requirements

To get this application up and running successfully, you need to meet the following requirements:
* System requirement:
    * Python 3
* Package requirements:
    * Tkinter
    * Matplotlib
    * Requests
    * Numpy

Don't worry about the package requirements. The next section, takes you through installing them.

# Installing 

To install the necessary packages for this application to run without errors, open the *school_python_project_2* folder in your terminal (or command prompt, or powershell), and run this command below:
```bash
pip install tk matplotlib requests numpy
```

# Starting up the application

Now that the project is set up, it's time to run the application. You can run this application by clicking your IDEs `run` button in *searcher.py*, or by running this command in your terminal:
```bash
python searcher.py
```

# How to compile

Compiling is the process of converting a high-level program (like this project) into machine code (an executable application). Once you compile, the project you'll be able to distrubute the application without the need for the users to have python installed in their system.

To compile this application, you need to first install `pyinstaller`:
```bash
pip install -U pyinstaller
```

Then, run this command to compile the project:
```bash
pyinstaller searcher.py
```

Once you run the command above, `pyinstaller` creates a directory called *dist*. Inside the *dist* folder, there'll be a *searcher* project folder.