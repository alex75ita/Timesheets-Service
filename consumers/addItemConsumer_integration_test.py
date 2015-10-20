from unittest import TestCase
from consumers.addItemConsumer import AddItemConsumer
from entities.configuration import Configuration


class AddItemConsumerTest(TestCase):


    def setUp(self):

        rabbitServer = ""
        rabbitHost = ""
        rabbitUser = "test"
        rabbitPassword = "test"
        self.configuration = Configuration(rabbitServer, rabbitHost, rabbitUser, rabbitPassword)

    def test_startConsuming(self):
        url = self.configuration.rabbitServer

        def messageReceivedCallback():
            pass

        consumer = AddItemConsumer(url, messageReceivedCallback)
        queue = "test"
        consumer.startConsuming(queue)


    def test_messageReceivedCallback(self):
        self.fail()

    def test_getDataFromMessage(self):
        self.fail("not implemented")
