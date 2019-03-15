# Particle-Swarm-Algorithm
The particle swarm optimization (PSO) algorithm, developed in 1995 by Kennedy and Eberhart, is based on the social behavior exhibited by animals such as birds or fish when they are working as a group to reach a destination. The algorithm can be used to find the global minimum or maximun of different types of functions. This project will create a PSO implementation to obtain the minimum of the Ackley Function.

1. Run program with shell script:

Make sure to change the directory in call_pso.sh to your local directory before running the program.
Run this in an environment that supports Bash on Windows such as Git Bash.

Command to run the program:

sh call_pso.sh <num_iteration> <num_particle> <value_of_w> <value_of_c1> <value_of_c2> <target_error>

2. Run program with batch script:

Make sure to change the directory in run_pso.bat to your local directory before running the program.
Run this in windows command prompt.

Command to run the program:
run_pso.bat <num_iteration> <num_particle> <value_of_w> <value_of_c1> <value_of_c2> <target_error>

3. Run program using python directly:

Run this in windows command prompt. In the directory of where particleswarm.py is, run command:
py or python ParticleSwarm.py <num_iteration> <num_particle> <value_of_w> <value_of_c1> <value_of_c2> <target_error>

4. Run program in an executable:

you can perform below in windows command prompt: 

1. download pyinstaller in a directory where python is installed. Command: pip install pyinstaller or py -m pip install pyinstaller
pyinstaller is installed in Scripts folder (every python folder has this).  

2. go to directory where python code is located. Run pyinstaller command to covert python code to executable, make sure to specify where your pyinstaller is. Also make sure to compile it along with numpy module. 
for me I used:
"c:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Scripts\pyinstaller
.exe" --hidden-import numpy ParticleSwarm.py

3. This will create a folder in /dist folder (you should have this in project folder) called ParticleSwarm along with ParticleSwarm.exe and all other dependencies
for me it is in C:\Users\yubo\PycharmProjects\Particle-Swarm-Algorithm\dist\ParticleSwarm

4. go to the directory that contains ParticleSwarm.exe and run command:
ParticleSwarm.exe <num_iteration> <num_particle> <value_of_w> <value_of_c1> <value_of_c2> <target_error>
