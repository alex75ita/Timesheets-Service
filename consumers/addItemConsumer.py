from datetime import date
import pika
from consumers import consumerBase
from consumers.consumerBase import ConsumerBase
from entities.item import Permit


class AddItemConsumer(ConsumerBase):
    """ Consumer for the message "AddItem"

    """

    def __init__(self, url, messageConsumedCallback):
        assert messageConsumedCallback is not None
        super().__init__(url)

        self.messageConsumedCallback = messageConsumedCallback

    def startConsuming(self, queue):
        """ Start to consume messages from the passed queue
        and call messageConsumed when message is managed
        """

        super().startConsuming()

        connection = super().getConnection()
        channel = connection.channel()
        channel.basic_consume(self._messageReceivedCallback,
                              queue=queue,
                              no_ack=True)

        channel.start_consuming()

    def _messageReceivedCallback(self, channel, method, properties, body):

        try:
            item = self._getItemFromMessage(body)
        except:
            raise Exception("Fail to get Item from message")

        self.messageConsumedCallback(item)

    @staticmethod
    def _getItemFromMessage(body):

        when = date(2015, 10, 4)
        hours = 3
        item = Permit(when, hours)

        return item
