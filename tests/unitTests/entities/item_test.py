from unittest import TestCase
import tests
import datetime
import entities.item
from entities.item import Item, Permit, PERMIT, HOLIDAY


class itemTest(TestCase):

    def test_parseDate(self):
        stringDate = "2015-12-31"
        date = entities.item._parseDate(stringDate)

        self.assertIsNotNone(date)
        self.assertIsInstance(date, datetime.date)
        self.assertEqual(2015, date.year)
        self.assertEqual(12, date.month)
        self.assertEqual(31, date.day)


class ItemTest(TestCase):

    def test_createItemFomData(self):
        when = tests._date
        hours = tests._hours
        data = {"kind": PERMIT, "date": when.isoformat(), "hours": hours}

        item_ = Item.createFromData(data)

        self.assertIsNotNone(item_)
        self.assertIsInstance(item_, Item)
        self.assertIsInstance(item_, Permit)
        self.assertEqual(when, item_.date)
        self.assertEqual(hours, item_.hours)


