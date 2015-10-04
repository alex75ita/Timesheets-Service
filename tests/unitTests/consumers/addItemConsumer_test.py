from unittest import TestCase
from consumers.addItemConsumer import AddItemConsumer
from entities.item import Permit, PERMIT, HOLIDAY
import datetime
import tests


class InsertItemConsumerTest(TestCase):

    def test__getItemFromMessage(self):
        url = None
        firstName = tests._firstName
        lastName = tests._lastName
        date = tests._date
        kind = PERMIT
        hours = tests._hours
        msg = '{{"employee": {{"firstName":"{firstName}", "lastName":"{lastName}"}}, "kind":"permit", "hours":"3"}}' \
            .format(firstName=firstName, lastName=lastName)

        def messageConsumedCallback():
            pass

        consumer = AddItemConsumer(url, messageConsumedCallback)
        item = consumer._getItemFromMessage(msg)

        self.assertIsNotNone(item)
        self.assertIsInstance(item, Permit)
        self.assertIsNotNone(item.date)
        self.assertIsNotNone(item.kind)
        self.assertIsNotNone(item.hours)
        self.assertEqual(item.date, date)
        self.assertEqual(item.kind, kind)
        self.assertEqual(item.hours, hours)
