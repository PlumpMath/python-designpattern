class AbstractConfig :
    storage = None

    def __init__(self, storage):
        self.storage = storage