from variables import data_dir, process_graph_file
from module.classes import Process, Message
from module.messaging import receive_message


def create_process_graph_from_file():
    processes = []
    try:
        f = open(data_dir + process_graph_file, "r")
        process_graph = f.readlines()
    except Exception as e:
        print(e)
        exit(1)

    try:
        process_count = len(process_graph)
        for index, i in enumerate(process_graph, 0):
            process = Process(p_no=index, process_count=process_count, dependents=i.strip())
            processes.append(process)
    except Exception as e:
        print(e)
    return processes


def display_process_dependents(processes):
    for process in processes:
        print(process.p_no, process.dependent)


def print_processes(processes):
    for process in processes:
        print(process)


def check_if_blocked_process(process):
    dependent = process.dependent
    # if sum of values in dependent array is greater than 1, the process is blocked.
    if sum(dependent) > 0:
        return True
    else:
        return False


def init_threads(process: Process):
    process.init_kafka()
    receive_message(process, check_if_blocked_process)


# def create_kafka_producer():
#     producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
#                              value_serializer=lambda x:
#                              dumps(x).encode('utf-8'))
#     return producer
