#!/bin/bash

function create(){
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
