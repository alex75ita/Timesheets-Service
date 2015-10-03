import unittest
import pika


_url = "amqp://rgryymew:5-V1Ax9_fTWtjIV9n1Jz_OOJ4hdbNlM3@baboon.rmq.cloudamqp.com/rgryymew"


class Consumer_test(unittest.TestCase):


    def test_startConsumikng(self):

        def callback(channel, method, properties, body):
            print(body)
            print("callback")

        params = pika.URLParameters(_url)
        params.socket_timeout = 5
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.basic_consume(callback,
            queue='test',
            no_ack=True)

        channel.start_consuming() # start consuming (blocks)