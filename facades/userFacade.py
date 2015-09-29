from entities.employee import Employee

class UserFacade:

    def __init__(self):
        self.connection = None

    def save(self, employee):
        #employee = Employee("AAA", "BBB")
        #client = MongoClient(self.dbServer, self.dbPort)
        #db = client[self.dbName]
        #document = employee.toJson()
        #id = db.employees.insert_one(document).inserted_id
        pass
