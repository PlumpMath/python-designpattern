from .Parameters import Parameters


class Connection :

    configuration = None
    host = None

    def __init__(self, config: Parameters):
        self.configuration = config

    def connect(self):
        self.host = self.configuration.get('host')

    def get_host(self):
        return self.host



