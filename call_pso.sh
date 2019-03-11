#!/bin/bash
#This script is to execute ParticleSwarm.py

pythonFile="/ParticleSwarm.py"
dirPath="$(pwd)"
filePath=$dirPath$pythonFile

/c/Users/yubo/AppData/Local/Programs/Python/Python36-32/Python.exe "$filePath" "$1" "$2" "$3" "$4" "$5"

