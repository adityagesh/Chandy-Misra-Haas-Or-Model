# from module.classes import Process
import multiprocessing
from module.functions import create_process_graph_from_file, print_processes, init_threads
from module.messaging import receive_message, send_query

import time
import random

# Read processes from file
processes = create_process_graph_from_file()
print_processes(processes)
threads = []

# Start kafka consumer for each process as individual threads
for process in processes:
    thread = multiprocessing.Process(target=init_threads, args=(process,))
    thread.start()
    threads.append(thread)

if __name__ == "__main__":
    # Define initiator process
    initiator = int(input("Enter initiator process number 0 to {}:".format(len(processes)-1)))
    try:
        if initiator < 0 or initiator > len(processes):
            raise IndexError
        process = processes[initiator]
        send_query(process, init=process.p_no)
    except IndexError:
        print("[ERROR] Exiting Program -- Process number is incorrect")
        for thread in threads:
            thread.terminate()
        exit()
    for thread in threads:
        thread.join()

# while True:
#     time.sleep(random.uniform(0, 5))
#     send_query(process, init=process.p_no)
for thread in threads:
    thread.join()
