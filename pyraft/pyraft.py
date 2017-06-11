from pyraft.servers.server import Follower





if __name__ == "__main__":
    NUM_SERVERS = 3
    servers = [
        Follower(id=i) for i in xrange(NUM_SERVERS)
    ]