from classes.Connection import Connection
from classes.ArrayConfig import ArrayConfig

# Dependency Injection
# Purpose : To implement a loosely coupled architecture in order to get better stable, maintainable and extendable code
# ArrayConfig is injected into Connection.
# A Connection (client) just use two functions get and set of config object is defined from an interface Parameters
# and don't care about how config object is implemented


config = ArrayConfig({})
config.set('host', 'localhost')

connection = Connection(config)
connection.connect()
print(connection.get_host())
