import pika


def send(msg):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='spy')
    channel.basic_publish(exchange='',
                          routing_key='spy',
                          body=msg)
    print(" [x] Sent 'hash'")
    connection.close()
    return hash
