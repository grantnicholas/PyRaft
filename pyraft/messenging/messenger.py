class Messenger(object):
    def post_message(self, message):
        pass

    def get_message(self, message):
        pass


class InMemoryMessenger(Messenger):
    def __init__(self):
        super(InMemoryMessenger, self).__init__()
        self.messenges = []

    def post_message(self, message):
        self.messenges.append(message)
        self.messenges = sorted(self.messenges, key=lambda m: m.timestamp, reverse=True)

    def get_message(self, message):
        try:
            return self.messenges.pop()
        except IndexError:
            return None
