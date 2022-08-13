from flask import Blueprint

bp_user = Blueprint('users', __name__, url_prefix='/users')


@bp_user.route('/', methods=['GET'])
def index():
    return 'index', 200


@bp_user.route('/', methods=['POST'])
def create():
    created = 2
    return 'create', 201, {
        'x-resource-id': created,
        'x-resource-uri': '/api/users/{}'.format(created)
    }


@bp_user.route('/<id>', methods=['PUT'])
def update(id):
    return 'update', 200, {
        'x-resource-id': id,
        'x-resource-uri': '/api/users/{}'.format(id)
    }


@bp_user.route('/<id>', methods=['DELETE'])
def delete(id):
    return 'delete', 204
