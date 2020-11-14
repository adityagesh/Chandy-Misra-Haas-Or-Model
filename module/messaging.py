from kafka import KafkaProducer
from json import dumps
from art import text2art
from module.classes import Message, Process
from kafka import KafkaProducer
from variables import kafka_broker


def send_message(process, topic, message):
    print("Process {} -> Process {} | Send message {}".format(process.p_no, topic, message))
    producer = KafkaProducer(bootstrap_servers=kafka_broker,
                             value_serializer=lambda x:
                             dumps(x).encode('utf-8'))
    producer.send(str(topic), value=message)
    producer.close()
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
            elif message.value['type'] == "reply":
                receive_reply(process, message.value)
        else:
            print("Process {} | Ignoring message: Reason: Process not blocked ".format(process.p_no))


def send_query(process, init):
    dependent = process.dependent
    for index, value in enumerate(dependent, 0):
        # check if process in dependent on i
        if value == 1:
            message = Message(message_type="query", init=init, src=process.p_no, dst=index)
            send_message(process, topic=index, message=message.get_value())
            process.num[init] += 1
            process.wait[init] = True


def receive_query(process: Process, value):
    init_process = value["data"][0]
    # If this is the engaging query
    if process.engaging_query is None:
        process.engaging_query = value["data"][1]
        send_query(process, init=init_process)
    else:
        if process.wait[init_process]:
            send_reply(process, value)


def send_reply(process: Process, value, engaging_dst=None):
    data = value["data"]
    if engaging_dst is None:
        dst = data[1]
    else:
        dst = engaging_dst
    message = Message(message_type="reply", init=data[0], src=process.p_no, dst=dst)
    send_message(process, topic=dst, message=message.get_value())


def receive_reply(process: Process, value):
    init_process = value["data"][0]
    if process.wait[init_process]:
        process.num[init_process] -= 1
        if process.num[init_process] == 0:
            if value["data"][0] == value["data"][2]:
                Art = text2art("DEAD LOCK DETECTED")
                print(Art)
            else:
                send_reply(process=process, value=value, engaging_dst=process.engaging_query)
