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

# Running the program 
 NOTE: The program is developed in **Ubuntu** OS
## Requirements
1. Docker & docker-compose
## Steps
The below commands are to be executed in the **root directory of the project**
1. To start kafka and zookeeper: Run `docker-compose up`. Keep the terminal open.  
2. To build the docker image of python program run `build-docker.sh` 
3. To execute the program, run `docker run -it --network=host aditya-deadlock-detection`     
4. Enter initiator process number in terminal   
5. Wait for 10 seconds - if deadlock exists, "DEADLOCK DETECTED" will be shown
6. Ctrl-C to exit  
7. Process dependency can be modified in `data/model.txt`, **Repeat from step 2** if input is changed.  



# Screenshot

![image](https://user-images.githubusercontent.com/26188281/99151465-6d589e80-26c1-11eb-959c-adfcd8a27fbe.png)


