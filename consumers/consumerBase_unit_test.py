#from ..consumers import ConsumerBase
from unittest import TestCase
from consumers.consumerBase import ConsumerBase


class ConsumerBaseTest(TestCase):

    def test_init(self):
        url = "aaa"
        consumer = ConsumerBase(url)

        assert consumer is not None

    def test_getConnection(self):

        consumer = ConsumerBase()
        connection = consumer.getConnection()

        self.assertIsNotNone(connection)

