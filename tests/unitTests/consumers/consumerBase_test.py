from test.test_exceptions import TestBase

from consumers import ConsumerBase


class ConsumerBaseTest(TestBase):

    def test_getConnection(self):

        consumer = ConsumerBase()
        connection = consumer.getConnection()

        self.assertIsNotNone(connection)

