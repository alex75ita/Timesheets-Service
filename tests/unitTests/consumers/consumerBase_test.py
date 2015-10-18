#from ..consumers import ConsumerBase
from unittest import TestCase
from consumers.consumerBase import ConsumerBase


class ConsumerBaseTest(TestCase):

    def test_getConnection(self):

        consumer = ConsumerBase()
        connection = consumer.getConnection()

        self.assertIsNotNone(connection)

