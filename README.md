saga-config
===========

This module is a python equivalent to the node.js config module found [here](https://www.npmjs.com/package/config).

## testing
```docker-compose up``` will automatically test the project and watch for changes.

To generate html coverage reports run:
`docker-compose run py tox -e html`

To run only the syntax linter run:
`docker-compose run py tox -e lint`

For more advanced testing see the tox.ini file.
