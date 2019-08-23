# Automating Project Initialization
The aim of the project was to be able to automate the repetitive process involved when initiating a new project.
In summary, the script makes a new local repository in the specified workspace directory, make a new online repository on the specified Github account, and then links the remote and local repositories by setting up an upstream.

### Prerequisites
Python modules needed:
* [PyGithub](https://pypi.org/project/PyGithub/) - Module used to connect to Github account

### Installation and Usage
```bash
git clone "https://github.com/IntrepidArrow/Automating-New-Projects-Setup.git"
cd Automating-New-Projects-Setup
source 
Then go to create.py and set the username and password to be your username and password.
Also make sure to change all directories to your directories so it should be '/Users/<your username>/path/to/your/project'
```