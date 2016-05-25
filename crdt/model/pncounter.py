import hot_redis

from crdt.constants import CLIENTS, DATA_TYPES, PN_COUNTER
from crdt.key_utilities import get_client_list_key, get_client_key, get_pcounter_key, get_ncounter_key
from crdt.redis_manager import connection
from crdt.model.gcounter import GCounter


class PNCounter:
    def __init__(self, key):
        # Setting the key of the PN Counter Instance
        self.key = key
        self.pcounter = GCounter(get_pcounter_key(key))
        self.ncounter = GCounter(get_ncounter_key(key))

        # Getting/Setting the client list and type of the GCounter instance
        self.client_list = hot_redis.Set(key=get_client_list_key(key), client=connection)
        hot_redis.Dict(key=DATA_TYPES, client=connection)[key] = PN_COUNTER

    def add_client(self, client_id):
        # Adding client ID to client list
        new_client = get_client_key(self.key, client_id)
        self.client_list.add(new_client)

        # Adding clients to component GCounters
        self.pcounter.add_client(client_id)
        self.ncounter.add_client(client_id)

    def get(self, client_id):
        pvalue = self.pcounter.get(client_id)
        nvalue = self.ncounter.get(client_id)
        count = pvalue - nvalue
        return count

    def set(self, client_id, pval, nval):
        self.pcounter.set(client_id, pval)
        self.ncounter.set(client_id, nval)

