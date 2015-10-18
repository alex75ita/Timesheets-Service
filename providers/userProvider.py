from pymongo.mongo_client import MongoClient
# from entities.employee import Employee

default_configuration = dict(server="127.0.0.1", port=27017, database="timesheets")


class UserProvider:

    def __init__(self, configuration=None):
        self.configuration = configuration or default_configuration

    def save(self, employee):
        print("save")
        client = MongoClient(self.configuration["server"], self.configuration["port"])
        db = client[self.configuration["database"]]
        document = employee.toJson()
        id_ = db.employees.insert_one(document).inserted_id
        #print(u"new id: {0}".format(id_))
