[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/9aHTYUBc)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=15187942)
# STEM103_Level3_1-ForLoop

# Program Overview 
Brian Sandstrom, June 2024, Stem 103 - Level 3 Create a Program using For Loop.\
A short Python script that analyzes a dataset and displays important information from it using for loops.
# Description
The main.py script takes the data from three provided lists of space mission data and generates a factual output.\
The datasets called mission_names, mission_years, and mission_success are analyzed by determining the total number of missions, the number of successful missions, and the number of missions before the year 2000.\
To create the data for those three variables, the script uses a for loop to generate it using if statements.\
Once that data is created, the script takes the number of successful missions with the total number of missions and calculates them with the formula (x/y) * 100 to find the success rate of all of the missions combined, which is then placed into a fourth variable.\
To display our factual output, data from three of the variables is then printed in the order of total mission numbers, successful mission numbers, and overall mission success rate.\
Finally, the script uses the fourth variable "MissionsPreY2K" and uses another for loop that prints out the name of each mission that happened before the year 2000.
