from unittest import TestCase

from consumers.addItemConsumer import AddItemConsumer
from entities.item import Permit, PERMIT
import tests


class InsertItemConsumerTest(TestCase):

    def test__getDataFromMessage_should_return_Item(self):
        url = None
        firstName = tests._firstName
        lastName = tests._lastName
        date = tests._date
        kind = PERMIT
        hours = tests._hours
        msg = '{{"employee": {{"firstName":"{firstName}", "lastName":"{lastName}"}}, \
            "date":"{date}", "kind":"{kind}", "hours":"{hours}"}}' \
            .format(firstName=firstName, lastName=lastName,
                    date=date.isoformat(), kind=kind, hours=hours)

        # print("msg: {0}".format(msg))

        def messageConsumedCallback():
            pass

        consumer = AddItemConsumer(url, messageConsumedCallback)
        data = consumer._getDataFromMessage(msg)

        self.assertIsNotNone(data)
        item = data[1]
        self.assertIsNotNone(item)
        self.assertIsInstance(item, Permit)
        self.assertIsNotNone(item.date)
        self.assertIsNotNone(item.kind)
        self.assertIsNotNone(item.hours)
        self.assertEqual(item.date, date)
        self.assertEqual(item.kind, kind)
        self.assertEqual(item.hours, hours)
