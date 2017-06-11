import time

class Message(object):
    def __init__(self,sender, receiver, term, data):
        self.timestamp = time.time()
        self.sender = sender
        self.receiver = receiver
        self.term = term
        self.data = data

class AppendEntry(Message):
    pass

class RequestVote(Message):
    pass

class RequestVoteResponse(Message):
    pass

class Response(Message):
    pass


MESSENGES = [cls for cls in globals().keys() if issubclass(cls, Message)]
