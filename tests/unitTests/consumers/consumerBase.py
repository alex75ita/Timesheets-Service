import unittest
from test.test_exceptions import TestBase
from consumers.consumerBase import ConsumerBase


class ConsumerBaseTest(TestBase):

    def test_getConnection(self):

        consumer = ConsumerBase()
        connection = consumer.getConnection()

        self.assertIsNotNone(connection)

