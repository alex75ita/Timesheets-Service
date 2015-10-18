import pika

_server = "bunny.cloudamqp.com"
_user = "fkfpctoh"
_password = "6yORM9AvfFYIhcv7pvO09GaTJsFvEpoi"
_url = "amqp://fkfpctoh:6yORM9AvfFYIhcv7pvO09GaTJsFvEpoi@bunny.cloudamqp.com/fkfpctoh"

# ref: https://www.rabbitmq.com/tutorials/tutorial-one-python.html


# import pika
# connection = pika.BlockingConnection()
# channel = connection.channel()
#
# for method_frame, properties, body in channel.consume('test'):
#
#     # Display the message parts and ack the message
#     print method_frame, properties, body
#     channel.basic_ack(method_frame.delivery_tag)
#
#     # Escape out of the loop after 10 messages
#     if method_frame.delivery_tag == 10:
#         break
#
# # Cancel the consumer and return any pending messages
# requeued_messages = channel.cancel()
# print 'Requeued %i messages' % requeued_messages
# connection.close()


class ConsumerBase:

    def __init__(self, url=None):
        self.url = url or _url

    def getConnection(self):
        params = pika.URLParameters(self.url)
        params.socket_timeout = 5
        connection = pika.BlockingConnection(params)
        return connection

    # def createUrl(self, server, user, password):
    #     url = "amqp://{user}".format(server)