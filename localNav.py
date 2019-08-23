import sys
import os
from github import Github, GithubException
 
# Enter Github login credentials here
username = "..."
password = "..."

# Enter workspace directory here with '\' at the end of path 
workspace = "C:\\Users\\abhi2\\PythonLearningCurve\\"

def create_project():
    # Access user account and make repo online
    try:
        status = os.makedirs(workspace+sys.argv[1])
        user = Github(username, password).get_user()
        if user.create_repo(sys.argv[1]): #Repo will be created on Github through conditional check here 
            print(f"Successfully created local directory in workspace and remote repository - {sys.argv[1]} - on Github")
        else:
            print(f"Unable to create remote repository {sys.argv[1]}") 

    except FileExistsError:
        print("Project with same name exists on system workspace directory.\nPlease try again.")

    except GithubException as e:
        if e.status == 422:
            print("Repository with same name already exists on this account.\nPlease try again.")
        elif e.status == 401:
            print("Invalid login credentials. Please check username or password specified in localNav script.")

        # Following line will only execute if Github error occurs but, the directory was still made in workspace directory
        os.rmdir(workspace+sys.argv[1])

if __name__ == "__main__":
    create_project()

