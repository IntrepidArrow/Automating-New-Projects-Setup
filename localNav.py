import sys
import os
from github import Github, GithubException
 

# Remove email and password credentials before committing to Git
username = "..."
password = "..."

workspace = "C:\\Users\\abhi2\\PythonLearningCurve\\"
status = os.makedirs(workspace+sys.argv[1])
# Access user account and make repo online
try:
    user = Github(username, password).get_user()
    if user.create_repo(sys.argv[1]): #Repo will be created on Github through conditional check here 
        print(f"Successfully created remote repository - {sys.argv[1]} - on Github")
    else:
        print(f"Unable to create remote repository {sys.argv[1]}") 

except GithubException:
    print("Exception Caught") # TODO: Change to see how specific messages can be displayed to the terminal 



