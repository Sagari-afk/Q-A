# DOCUMENTATION for Q-A


## Introduction

Q-A is a command-line interface program that allows users to ask and answer questions on various topics.

## Prerequisites

To use the program, you'll need to have Python 3.x installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).


## Installation

1. Clone the repository to your local machine using the command:

```bash
git clone https://github.com/Sagari-afk/Q-A.git
```

2. Navigate to the directory where the repository was cloned:

```bash
cd Q-A
```


## Usage

To start the program, run the following command from the project directory in console:
```bash
python3 main.py
```


## Architecture
The Q-A program is built using Python 3.x and consists of the following modules:

+ `api_call.py`: This is the module that contains contains a class named MakeApiCall which is used to make API calls to get data from a web service
+ `lucy.py`: This is the module that contains class Lucy which is responsible for creating teams, adding and subtracting team scores, and outputting it
+ `main.py`: This is the main module that contains the GamePlay class, which is responsible for running the program
+ `text_const.py`: Contains text constants for later usage
+ `validators.py`: This is the module thad make response data better to use


## Conclusion
That's it! You now have a basic understanding of the Q-A codebase and how to contribute to the project. If you have any questions or need further assistance, please don't hesitate to contact the project owner or open an issue on GitHub.
