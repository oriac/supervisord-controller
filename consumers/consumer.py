#!/usr/bin/env python
import pika, time

time.sleep(10)  # delays for 5 seconds

connection = pika.BlockingConnection(pika.ConnectionParameters(host='message_broker'))
channel = connection.channel()

channel.queue_declare(queue='test')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(
    callback,
    queue='test',
    no_ack=True
)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()



