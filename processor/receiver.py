import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='spy')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode('utf-8'))


def consume():
    channel.basic_consume(callback,
                          queue='spy',
                          no_ack=True)
    channel.start_consuming()


consume()
