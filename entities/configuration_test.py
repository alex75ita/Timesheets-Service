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

    def createRabbitUrl(self):

        server = "test"
        host = "host"
        user = "user"
        password = "password"
        expectedUrl = "ampq://user:password@server/host"

        config = Configuration(server, host, user, password)

        url = config.createRabbitUrl()

        assert url is not None
        assert isinstance(url, str)
        assert url == expectedUrl

    def createRabbitUrl_when_passwordContainsChiocciola(self):

        server = "test"
        host = "host"
        user = "user"
        password = "p@ssword"
        expectedUrl = "ampq://user:p%40ssword@server/host"

        config = Configuration(server, host, user, password)

        url = config.createRabbitUrl()

        assert url is not None
        assert isinstance(url, str)
        assert url == expectedUrl
