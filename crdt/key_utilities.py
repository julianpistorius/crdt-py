from constants import CLIENTS


def get_client_list_key(key):
    return key + '_' + CLIENTS


def get_client_key(key, client_id):
    return key + '_' + client_id


def get_pcounter_key(key):
    return key + 'P'


def get_ncounter_key(key):
    return key + 'N'

