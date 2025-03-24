FCFS Simulation

📌 Project Description

This project is a First Come, First Served (FCFS)and SJF algorithm simulator, which are the fundamental scheduling algorithms in operating systems. The program takes a set of tasks and simulates their execution based on arrival order and burst time.
🛠️ Technologies

Python 3.11

Standard Python libraries

Systemy_FCFS_and_SJF/
├── main.py             # Main file to run the simulation
├── config.py           # Configuration parameters
├── schedule.py         # Module managing task scheduling
├── task.py             # Task class definition
├── utils.py            # Helper functions
├── test_data/          # Sample input files
└── wyniki_eksperymentow.csv  # Simulation results

Run the simulation:
python main.py

This simulation works on 100 sequences with 100 tasks each. Each task has random time arrival and burst time. Example used data is saved in test_data
Example output is given wyniki_eksperymentow.csv and it will be the place where everythnig will be saved. There is also a comparison of overall time that is required for each algorithm at the bottom of the .csv file.


This project is licensed under the MIT License. You are free to modify and use it in your own projects.

