#!/bin/bash
#This script is to execute ParticleSwarm.py

pythonFile="/ParticleSwarm.py"
dirPath="$(pwd)"
filePath=$dirPath$pythonFile

/c/Program\ Files\ \(x86\)/Microsoft\ Visual\ Studio/Shared/Python36_64/Python.exe "$filePath" "$1" "$2" "$3" "$4" "$5" "$6"

