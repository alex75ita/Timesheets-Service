
class Configuration:


    def __init__(self, rabbitServer, rabbitHost, rabbitUser, rabbitPassword):

        assert rabbitServer is not None
        assert rabbitHost is not None
        assert rabbitUser is not None
        assert rabbitPassword is not None

        self.rabbitServer = rabbitServer
        self.rabbitHost = rabbitHost
        self.rabbitUser = rabbitUser
        self.rabbitPassword = rabbitPassword


