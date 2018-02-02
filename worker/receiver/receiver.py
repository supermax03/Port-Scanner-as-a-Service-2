import pika
import json
from dao.dataaccesslayer import addoperation

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='spy')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode('utf-8'))
    msg=json.loads(body.decode('utf-8'))
    print(msg[0])
    addoperation(msg[0])



def consume():
    channel.basic_consume(callback,
                          queue='spy',
                          no_ack=True)
    channel.start_consuming()


consume()
