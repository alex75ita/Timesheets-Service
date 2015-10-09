import pika

_server = "bunny.cloudamqp.com"
_user = "fkfpctoh"
_password = "6yORM9AvfFYIhcv7pvO09GaTJsFvEpoi"
_url = "amqp://fkfpctoh:6yORM9AvfFYIhcv7pvO09GaTJsFvEpoi@bunny.cloudamqp.com/fkfpctoh"


class ConsumerBase:

    def __init__(self, url=None):
        self.url = url or _url

    def getConnection(self):
        params = pika.URLParameters(_url)
        params.socket_timeout = 5
        connection = pika.BlockingConnection(params)
        return connection

    # def createUrl(self, server, user, password):
    #     url = "amqp://{user}".format(server)