import pika

_host = "http:"

_server = "bunny.cloudamqp.com"
_user = "fkfpctoh"
_password = "6yORM9AvfFYIhcv7pvO09GaTJsFvEpoi"
_url = "amqp://fkfpctoh:6yORM9AvfFYIhcv7pvO09GaTJsFvEpoi@bunny.cloudamqp.com/fkfpctoh"


_user = "rgryymew"
_password = "5-V1Ax9_fTWtjIV9n1Jz_OOJ4hdbNlM3"
_url = "amqp://rgryymew:5-V1Ax9_fTWtjIV9n1Jz_OOJ4hdbNlM3@baboon.rmq.cloudamqp.com/rgryymew"

class Sender:

    def testConnection(self):
        #params = pika.ConnectionParameters(_url)
        #params.heartbeat = 5

        params = pika.URLParameters(_url)
        params.socket_timeout = 5

        #connection = pika.BlockingConnection(pika.ConnectionParameters(_url))
        connection = pika.BlockingConnection(params)

    def sendMessage(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(_url))
        channel = connection.channel()
        channel.queue_declare("aaa")