from datetime import date
import datetime
import sys

HOLIDAY = "holiday"
PERMIT = "permit"


class Item:

    def __init__(self, when, kind, hours=None):
        assert isinstance(when, date)
        assert kind in [HOLIDAY, PERMIT]
        self.date = when
        self.kind = kind
        if self.kind == PERMIT:
            assert hours is not None
            self.hours = int(hours)

    @staticmethod
    def createFromData(data):

        """Create the Permit or Holiday item from the passed data.
        "data" is a dictionary obtained from JSON message.

        :rtype : Item
        """

        assert "kind" in data.keys()
        assert "date" in data.keys()

        kind = data["kind"]
        isPermit = kind == PERMIT
        if isPermit:
            assert "hours" in data.keys()

        when = _parseDate(data["date"])

        if isPermit:
            hours = data["hours"]
            _item = Permit(when, hours)
        else:
            _item = Holiday(when)

        return _item


class Permit(Item):
    def __init__(self, when, hours):
        super().__init__(when, PERMIT, hours)


class Holiday(Item):
    def __init__(self, when):
        super().__init__(when, HOLIDAY)

def _parseDate(stringDate):
    try:
        return datetime.datetime.strptime(stringDate, "%Y-%m-%d").date()
    except:
        raise Exception("Fail to parse date: `\"{0}\".".format(stringDate), sys.exc_info()[1])