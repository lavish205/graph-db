import happybase
from table_config import get_table_config

class HConnection(object):

    connection = None
    def __init__(self, hostname):
        self.hostname = hostname

    def connect(self):
        print self.hostname
        if self.connection is not None:
            return self.connection

        self.connection = happybase.Connection(self.hostname)
        self.init()
        return self.connection

    def init(self):
        tables = self.connection.tables()
	config = get_table_config()
	for tb_obj in config:
	    table_name = tb_obj['table_name']
            if table_name in tables:
                continue
            config = {k:dict() for k in tb_obj["cfs"]}
	    self.connection.create_table(table_name, config)

