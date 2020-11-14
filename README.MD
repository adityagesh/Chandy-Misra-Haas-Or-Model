# Assumptions
1. Only one process initiates a query message  
2. A process with at least one dependency on another process is called a blocked process  
3. A process without dependency on any other process is a non blocked process. This process ignores the deadlock detection algorithm  
4. Process id's are continuous from 0 to n-1. 

# Defining the Process graph
1. data/model.txt contains the process graph input  
2. Each line defines a process. Processes are numbered from 0 to n-1  
3. To represent dependency of process 0 on process 4, enter '4' in line 1 of model.txt  
4. To represent dependency of process 2 on process 1 and 4, enter '1 4' on line 3 of model.txt  
5. If the process does not have any dependency, add a newline (without blank space)  

