from app.core.connection import Connection
from app.core.observer import Observer
from app.test_session import TestSession

observer = Observer()
connection = Connection(host="localhost", port=8080)

observer.register('connected') # create observe event
observer.register('test') # create observe event

connection.connect(observer)

test_session = TestSession()

observer.subscribe('test', test_session.test)
observer.subscribe('test', test_session.test_v2)

connection.run()