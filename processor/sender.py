import pika
from myutils.utils import gethash


def send():
    hash = gethash()
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='spy')
    channel.basic_publish(exchange='',
                          routing_key='spy',
                          body=hash)
    print(" [x] Sent 'hash'")
    connection.close()
    return hash
