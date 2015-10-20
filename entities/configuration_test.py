from unittest import TestCase
from entities.configuration import Configuration


class ConfigurationTest(TestCase):

    def test_init(self):

        server = "test"
        host = "host"
        user = "user"
        password = "password"

        config = Configuration(server, host, user, password)

        assert config is not None
        assert config.rabbitServer == server
        assert config.rabbitHost == host
        assert config.rabbitUser == user
        assert config.rabbitPassword == password


