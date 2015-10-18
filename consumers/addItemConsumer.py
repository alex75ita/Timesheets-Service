import json
import sys

from consumers.consumerBase import ConsumerBase
from entities.item import Item


class AddItemConsumer(ConsumerBase):
    """ Consumer for the message "AddItem"

    """

    def __init__(self, url, messageConsumedCallback):
        assert isinstance(url, str) is True
        assert messageConsumedCallback is not None
        super().__init__(url)

        self.messageConsumedCallback = messageConsumedCallback

    def startConsuming(self, queue):
        """ Start to consume messages from the passed queue
        and call messageConsumed when message is managed
        :param queue: name of the queue
        :type queue: string
        """

        assert isinstance(queue, str) is True


        connection = super().getConnection()
        channel = connection.channel()
        channel.basic_consume(self._messageReceivedCallback,
                              queue=queue,
                              no_ack=True)
        #todo: stop consuming after a while
        #channel.start_consuming()

    def _messageReceivedCallback(self, channel, method, properties, body):

        try:
            data = self._getItemFromMessage(body)
        except:
            raise Exception("Fail to get Item from message")

        self.messageConsumedCallback(data)

    @staticmethod
    def _getDataFromMessage(body):

        if body == "Quit":
            raise Exception("Message body: \"Quit\".")

        try:
            data = json.loads(body)
        except:
            raise Exception("Fail to parse JSON.", sys.exc_info()[1])

        assert "employee" in data.keys()

        employee = None  # Employee.create #todo
        item_ = Item.createFromData(data)

        return employee, item_
