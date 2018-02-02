import pika
from dao.dataaccesslayer import dal
from dao.entities import Operation
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='spy')


def callback(ch, method, properties, body):

    payload=json.loads(body)
    print(payload[0])
    print(payload[0]['hash'])



def consume():
    channel.basic_consume(callback,
                          queue='spy',
                          no_ack=True)
    channel.start_consuming()


consume()
