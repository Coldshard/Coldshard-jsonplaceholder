JSONPLACEHOLDER_HOST = 'https://jsonplaceholder.typicode.com'


class ParamTypes:

    types = {
        'userId': 'int',
        'id': 'int',
        'title': 'str',
        'completed': 'bool'
    }


class ResourceLimits:

    limits = {
        'posts': 100,
        'comments': 500,
        'albums': 100,
        'photos': 5000,
        'todos': 200,
        'users': 10,
    }


class ResourceData:

    data = {
        'todo': ['userId', 'id', 'title', 'completed']
    }
