# Automating Project Initialization
The aim of the project was to be able to automate the repetitive process involved when initiating a new project.
In summary, the script makes a new local repository in the specified workspace directory, make a new online repository on the specified Github account, and then links the remote and local repositories by setting up an upstream.

### Prerequisites
Python modules needed:
* [PyGithub](https://pypi.org/project/PyGithub/) - Module used to connect to Github account

### Installation and Usage
* Dot Source method
```bash
git clone "https://github.com/IntrepidArrow/Automating-New-Projects-Setup.git"
cd Automating-New-Projects-Setup
Go to localNav.py and set the workspace directory, username and password to be your Github username and password
source commands.sh or . commands.sh in bash terminal 

Finally, to run the script type in 'create <Name of project>'
```

### Alternate usage (Editing .bash_profile)
An issue with the above method of usage is that for every new bash session, user has to navigate to Automating-New-Projects-Setup directory first and dot source the shell script to invoke the "create" function for that session.
A different solution is to edit the .bash_profile and writing a create() (or any other function name preference) function that can be invoked for any bash session. The body of the function will be the same body of the create() function written in the commands.sh script. Here is what your function in your bash profile should look like at the end:

```bash
create() {
    cd C:\\Users\\abhi2\\PythonLearningCurve\\Project_setup_automation
    python localNav.py $1
    cd C:\\Users\\abhi2\\PythonLearningCurve\\$1
    git init
    touch README.md
    git add .
    git commit -m "Initial commit"
    git remote add origin https://github.com/IntrepidArrow/$1.git
    git push -u origin master
    code .
}
```

The advantage of the alternate method is that you do not need to navigate to the Automating-New-Projects-Setup directory and dot source the command.sh shell script for every new bash session. This method is permament and make the "create" function readily available for every bash session.