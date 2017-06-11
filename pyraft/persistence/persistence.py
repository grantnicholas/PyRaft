import shove

class DB:
    """
    Simple key-value based DB backend
    This can be any disk-backed ACID persistence engine
    """
    db_path = "/tmp/"

    def __init__(self, id):
        self.id = id
        self.store = shove.Shove(
            "file://{}".format(DB.db_path + self.id)
        )

    def __setitem__(self, key, value):
        self.store[key] = value

    def __getitem__(self, item):
        return self.store[item]
