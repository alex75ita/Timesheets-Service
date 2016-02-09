from threading import Thread
import pika
import time


class ConsumerBase:

    def __init__(self, url, queue):
        assert url is not None
        assert queue is not None

        self.isStopRequested = False
        self.url = url
        self.queue = queue

    def getConnection(self):
        params = pika.URLParameters(self.url)
        params.socket_timeout = 5
        connection = pika.BlockingConnection(params)
        return connection

    # def createUrl(self, server, user, password):
    #     url = "amqp://{user}".format(server)


    def startConsuming(self):

        # ref: https://www.rabbitmq.com/tutorials/tutorial-one-python.html

        thread = Thread(target=self._consume(), args=())
        thread.Start()


    def stopConsuming(self):

        self.isStopRequested = True


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


    def _consume(self):

        connection = self.getConnection()
        channel = connection.channel()

        noAck = True

        while not self.isStopRequested:

            for methodFrame, properties, body in channel.consume(queue, no_ack=noAck):

                # Display the message parts and ack the message
                print("methodFrame: {0}, properties: {1}, body: {2}".format(methodFrame, properties, body))
                channel.basic_ack(methodFrame.delivery_tag)

                # exit if required
                if self.isStopRequested:
                    break

            time.sleep(5)

        channel.cancel()
        channel.close()