from random import choice, randrange
from string import ascii_letters
from config import ParamTypes, ResourceData


def generate_integer(min, max):
    return randrange(min, max)


def generate_string(min, max):
    return ''.join(choice(ascii_letters) for _ in range(min, max))


def prepare_single_data(param, positive=True, limit=10):
    (min, max) = (1, limit) if positive else (limit+1, limit*2)
    type = ParamTypes.types[param]
    data = ''
    if type == 'int':
        data = generate_integer(min, max)
    elif type == 'str':
        data = generate_string(min, max)
    elif type == 'bool':
        data = generate_integer(0, 1)
    return data


def prepare_mass_data(resource):
    return {res: prepare_single_data(res) for res in ResourceData.data[resource]}
