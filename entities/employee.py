class Employee:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def toJson(self):
        return {"firstName": self.firstName, "lastName": self.lastName}

