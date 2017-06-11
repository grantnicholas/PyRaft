from pyraft.persistence.persistence import DB
from pyraft.messenging.message import AppendEntry, RequestVote, RequestVoteResponse, Response


class Server:
    def __init__(self, id, log, nodes, messenger):
        self.id =  id
        self.log = log
        self.current_term = 0
        self.nodes = nodes
        self.messenger = messenger
        self.timeout = 1
        self.db = DB(id=id)
        self.on_init()

    def on_init(self):
        self.current_term += 1

    def write_log(self, key, value):
        self.db[key] = value

    def send_message(self, message):
        for n in self.nodes:
            n.messenger.post_message(message)

    def send_message_response(self, message):
        node = [n for n in self.nodes if n.id == message.receiver]
        if len(node) > 0:
            node[0].messenger.post_message(message)

    def recv_message(self, message):
        if message.term > self.current_term:
            self.current_term = message.term
        elif message.term < self.current_term:
            pass # let them know they are behind the current term # self.send_message()

        self.match(message)

    def match(self, message):
        return {
            AppendEntry: self.on_append_entry,
            RequestVote: self.on_vote_request,
            RequestVoteResponse: self.on_vote_received,
            Response: self.on_response_received
        }[type(message)](message)

    def on_leader_timeout(self, message):
        pass

    def on_vote_request(self, message):
        pass

    def on_vote_received(self, message):
        pass

    def on_append_entry(self, message):
        pass

    def on_response_received(self, message):
        pass

    def on_client_command(self, message):
        pass


    def nextTimeout(self):
        import time
        import random
        self._currentTime = time.time()
        return self._currentTime + random.randrange(self.timeout, 2 * self.timeout)




class Leader(Server):
    pass


class Follower(Server):
    pass


class Candidate(Server):
    pass