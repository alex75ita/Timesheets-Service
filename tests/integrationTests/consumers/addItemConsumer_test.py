from unittest import TestCase
from consumers.addItemConsumer import AddItemConsumer
from tests.integrationTests import consumers


class AddItemConsumerTest(TestCase):

    def test_startConsuming(self):
        url = consumers.getUrl()

        def messageReceivedCallback():
            pass

        consumer = AddItemConsumer(url, messageReceivedCallback)
        queue = "test"
        consumer.startConsuming(queue)



    def test__messageReceivedCallback(self):
        self.fail()

    def test__getDataFromMessage(self):
        self.fail()
