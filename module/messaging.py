from kafka import KafkaProducer
from json import dumps

from module.classes import Message, Process
from kafka import KafkaProducer


def send_message(process, topic, message):
    print("Send message {} by {} to process {}".format(message, process.p_no, topic))
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda x:
                             dumps(x).encode('utf-8'))
    producer.send(str(topic), value=message)
    # if producer is None:
    #     process.producer.send(str(topic), value=message)
    # else:
    #     print(producer)
    #     producer.send(str(topic), value=message)


def receive_message(process, check_if_blocked_process):
    for message in process.consumer:
        if check_if_blocked_process(process):
            # Convert JSON list back to tuple
            message.value['data'] = tuple(message.value['data'])
            print("Process {} | Received message {}".format(process.p_no, message.value))
            if message.value['type'] == "query":
                receive_query(process, message.value)
        else:
            print("Process {} | Ignoring message: Reason: Process not blocked ".format(process.p_no))


def send_query(process, init):
    dependent = process.dependent
    for index, value in enumerate(dependent, 0):
        # check if process in dependent on i
        if value == 1:
            message = Message(message_type="query", init=init, src=process.p_no, dst=index)
            send_message(process, topic=index, message=message.get_value())
            process.num[process.p_no] += 1
            process.wait[process.p_no] = True


def receive_query(process: Process, value):
    init_process = value["data"][0]
    # If this is the engaging query
    if process.engaging_query:
        process.engaging_query = False
        send_query(process, init=init_process)
    else:
        if process.wait[init_process]:
            send_reply(process)


def send_reply(process: Process):
    pass
