import unittest
from pymongo.mongo_client import MongoClient

class userFacadeTsts(unittest.TestCase):

    def test_save_create_a_record_in_database(self):
        self.fail("not implemented")

    def test_connection(self):
        dbServer = "mongodb://213.136.84.88"
        port = 27017
        client = MongoClient(dbServer, port)
        self.assertIsNotNone(client)