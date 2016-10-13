"""This is an example config file."""
from os import environ

# The config is a python dict
config = {
    # It can therefore contain any type supported by python.
    'default_string': 'string',
    'default_int': 0,
    'default_nested': {
        'default_int': 0,
        'default_string': 'string'
    },

    # It can also call code
    'default_env': environ.get('RUN_ENV'),

    # Or simply be null.
    'default_empty': None,
}
