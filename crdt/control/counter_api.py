import hot_redis
from flask import Blueprint, request

from crdt.constants import DATA_TYPES, G_COUNTER
from crdt.generate_key import generate_random_crdt_key
from crdt.redis_manager import connection
from crdt.model.gcounter import GCounter


counter_api_blueprint = Blueprint('Counter', __name__)


@counter_api_blueprint.route("/g/new", methods=['GET'])
def new_g_counter():
    key = request.args.get('key')
    client_id = request.args.get('client_id')
    # TODO: check if client_id valid
    if key is not None or len(key)==0:
        key = generate_random_crdt_key()
    if key in hot_redis.Dict(key=DATA_TYPES, client=connection).keys()\
        or hot_redis.Dict(key=DATA_TYPES, client=connection)[key] is not G_COUNTER:
        # TODO: return type fail
        pass
    else:
        new_g_counter = GCounter(key=key)
        new_g_counter.add_client(client_id)

    # TODO: send success


@counter_api_blueprint.route("/g/set", methods=['GET'])
def set_g_counter():
    key = request.args.get('key')
    client_id = request.args.get('client_id')
    value = request.args.get('value')
    if key is not None or len(key) == 0:
        key = generate_random_crdt_key()
    if key in hot_redis.Dict(key=DATA_TYPES, client=connection).keys() \
            or hot_redis.Dict(key=DATA_TYPES, client=connection)[key] is not G_COUNTER:
        # TODO: return type fail
        pass
    else:
        g_counter = GCounter(key=key)
        g_counter.set(client_id, value)

    # TODO: send success


@counter_api_blueprint.route("/g/get", methods=['GET'])
def get_g_counter():
    key = request.args.get('key')
    client_id = request.args.get('client_id')
    value = request.args.get('value')
    if key is not None or len(key) == 0:
        key = generate_random_crdt_key()
    if key in hot_redis.Dict(key=DATA_TYPES, client=connection).keys() \
            or hot_redis.Dict(key=DATA_TYPES, client=connection)[key] is not G_COUNTER:
        # TODO: return type fail
        pass
    else:
        g_counter = GCounter(key=key)
        counter = g_counter.get(client_id)
        # TODO: send counter value in success


# @counter_api_blueprint.route("/pn/new", methods=['GET'])
# def new_pn_counter():
#
#
# @counter_api_blueprint.route("/pn/update", methods=['GET'])
# def update_pn_counter_state():
