from datetime import date

HOLIDAY = 1
PERMIT = 2


class Item:

    def __init__(self, when, kind, hours=None):
        assert isinstance(when, date)
        assert kind in [HOLIDAY, PERMIT]
        self.date = when
        self.kind = kind
        if self.kind == PERMIT:
            assert hours is not None
            self.hours = hours


class Permit(Item):
    def __init__(self, when, hours):
        super().__init__(when, PERMIT, hours)


class Holiday(Item):
    def __init__(self, when):
        super().__init__(when, HOLIDAY)