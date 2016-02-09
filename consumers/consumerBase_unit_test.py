#from ..consumers import ConsumerBase
from unittest import TestCase
from consumers.consumerBase import ConsumerBase
from consumers import configuration

class ConsumerBaseTest(TestCase):

    def test_init(self):
        url = configuration["url"]
        queue = configuration["queue"]
        consumer = ConsumerBase(url)

        assert consumer is not None

    def test_getConnection(self):

        consumer = ConsumerBase()
        connection = consumer.getConnection()

        self.assertIsNotNone(connection)

