import pika
from consumers import consumerBase


class Consumer(consumerBase):

    def startConsuming(self, params):

        connection = pika.BlockingConnection(params)
        connection.channel().start_consuming()