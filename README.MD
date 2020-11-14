# Assumptions
1. Only one process initiates a query message  
2. A process with at least one dependency on another process is called a blocked process  
3. A process without dependency on any other process is a non blocked process. This process ignores the deadlock detection algorithm  
4. Process id's are continuous from 0 to n-1. 
5. A message "Deadlock detected" is shown if there is a deadlock, otherwise no message is displayed.
6. Console messages might be printed even after "Deadlock detected" is shown since each process is independent of the other and consumes from different kafka topics.

# Defining the Process graph
1. data/model.txt contains the process graph input  
2. Each line defines a process. Processes are numbered from 0 to n-1  
3. To represent dependency of process 0 on process 4, enter '4' in line 1 of model.txt  
4. To represent dependency of process 2 on process 1 and 4, enter '1 4' on line 3 of model.txt  
5. If the process does not have any dependency, add a newline (without blank space)  

# Running the program - method 1
 NOTE: The following contains the commands to run in **Ubuntu**
## Requirements
1. Docker & docker-compose
2. Python
## Steps
The below commands are to be executed in the root directory of the project
1. To start kafka and zookeeper: Run `docker-compose up`  
2. Create virtual environment: `python -m venv venv`  
3. Activate virtual environment: `source venv/bin/activate`  
4. Install requirements: `pip install -r requirements.txt`   
5. Process dependency can be modified in `data/model.txt`  
6. Run the program:  `python run.py`  
7. Enter initiator process number in terminal (values from 0 to n-1)  
8. Ctrl-C to exit  

# Running the program - method 2
 NOTE: The following contains the commands to run in **Ubuntu**
## Requirements
1. Kafka & Zookeeper
2. Python
## Steps
The below commands are to be executed in the root directory of the project
1. Create virtual environment: `python -m venv venv`  
2. Activate virtual environment: `source venv/bin/activate`  
3. Install requirements: `pip install -r requirements.txt`  
4. Change host in module/variables.py. Variable name: `kafka_broker`  
5. Process dependency can be modified in `data/model.txt`  
6. Run the program:  `python run.py`  
7. Enter initiator process number in terminal (values from 0 to n-1)  



