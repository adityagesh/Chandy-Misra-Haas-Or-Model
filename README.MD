# Assumptions
1. Only one process initiates a query message  
2. A process with at least one dependency on another process is called a blocked process  
3. A process without dependency on any other process is a non blocked process. This process ignores the deadlock detection algorithm  
4. Process id's are continuous from 0 to 9. 
5. A message "Deadlock detected" is shown if there is a deadlock, otherwise no message is displayed.
6. Console messages might be printed even after "Deadlock detected" is shown since each process is independent of the other and consumes from different kafka topics.

# Defining the Process graph
1. data/model.txt contains the process graph input  
2. Each line defines a process. Processes are numbered from 0 to 9  
3. To represent dependency of process 0 on process 4, enter '4' in line 1 of model.txt  
4. To represent dependency of process 2 on process 1 and 4, enter '1 4' on line 3 of model.txt  
5. If the process does not have any dependency, add a newline (without space)  

# Running the program - method 1 [RECOMMENDED]
 NOTE: The program is developed in **Ubuntu** OS
## Requirements
1. Docker & docker-compose
## Steps
The below commands are to be executed in the **root directory of the project**
1. To start kafka and zookeeper: Run `docker-compose up`. Wait for kafka to start and keep the terminal open.  
2. To build the docker image of python program run `build-docker.sh` 
3. To execute the program, run `docker run -it --network=host aditya-deadlock-detection`     
4. Enter initiator process number in terminal   
5. Wait for 10 seconds - if deadlock exists, "DEADLOCK DETECTED" will be shown
6. Ctrl-C to exit  
7. Process dependency can be modified in `data/model.txt`, **Repeat from step 2** if changed.  
8. Close the terminal running kafka and zookeeper (step 1)  

# Running the program - method 2
 NOTE: The following contains the commands to run in **Ubuntu**
## Requirements
1. Python
2. Kafka & Zookeeper
## Steps
The below commands are to be executed in the root directory of the project
1. Create virtual environment: `python -m venv venv`  
2. Activate virtual environment: `source venv/bin/activate`  
3. Install requirements: `pip install -r requirements.txt`  
4. Change host in variables.py. Variable name: `kafka_broker` 
5. Run the program:  `python run.py` 
6. Enter initiator process number in terminal   
7. Wait for 10 seconds - if deadlock exists, "DEADLOCK DETECTED" will be shown
8. Ctrl-C to exit  
9. Process dependency can be modified in `data/model.txt` 
10. Repeat from step 5, if process dependency is changed
 

# Screenshot
1. Input
![image](https://user-images.githubusercontent.com/26188281/99181434-937b4e80-2754-11eb-8d9b-8cb1f15b93a4.png)

2. Output
![image](https://user-images.githubusercontent.com/26188281/99151465-6d589e80-26c1-11eb-959c-adfcd8a27fbe.png)


