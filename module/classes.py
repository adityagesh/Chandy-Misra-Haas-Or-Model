from kafka import KafkaConsumer, KafkaProducer
from json import dumps, loads
from variables import kafka_broker


class Process:
    def __init__(self, p_no, process_count, dependents):
        self.p_no = p_no
        self.site = 0
        self.dependent = [0] * process_count
        # number of query messages sent
        self.num = [0] * process_count
        # wait[i] denotes process is blocked since the last engaging query received from Pi
        self.wait = [False] * process_count
        self.create_dependents(dependents=dependents, process_count=process_count)
        self.consumer = None
        self.producer = None
        self.engaging_query = None

    def create_dependents(self, dependents: str, process_count):
        if len(dependents) == 0:
            return
        else:
            dependents = dependents.replace(" ", "")
            for i in dependents:
                if int(i) >= process_count:
                    print("Incorrect dependency number in model.txt")
                    exit(0)
                else:
                    self.dependent[int(i)] = 1

    def initiate_deadlock_detection(self):
        # send query(i, i, j) to all processes Pj in the dependent set DSi
        # numi(i) = |DSi|
        # waiti(i) = true
        pass

    def __str__(self):
        return "Process: {} | dependent: {} | num: {} | wait {}".format(self.p_no, self.dependent, self.num, self.wait)

    def init_kafka(self):
        self.producer = KafkaProducer(bootstrap_servers=kafka_broker,
                                      value_serializer=lambda x:
                                      dumps(x).encode('utf-8'))
        self.consumer = KafkaConsumer(str(self.p_no),
                                      group_id=str(self.p_no),
                                      bootstrap_servers=kafka_broker,
                                      auto_offset_reset='latest',
                                      enable_auto_commit=False,
                                      value_deserializer=lambda x: loads(x.decode('utf-8')))


class Message:
    def __init__(self, message_type, init, src, dst):
        self.message_type = message_type
        self.message = self.create_message(init, src, dst)

    def create_message(self, init, src, dst):
        message = {"type": self.message_type}
        message.update({"data": (init, src, dst)})
        return message

    def get_value(self):
        return self.message
