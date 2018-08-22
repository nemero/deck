from app.core.connection import Connection
from app.core.observer import Observer
from app.test_session import TestSession

observer = Observer()
connection = Connection(host="localhost", port=8080)

observer.register('message') # create observe event
observer.register('system') # create observe event

observer.register('test') # create observe event

connection.connect(observer)

test_session = TestSession()

observer.subscribe('message', test_session.test)
observer.subscribe('test', test_session.test)
observer.subscribe('test', test_session.test_v2)
observer.subscribe('system', test_session.online)

connection.run()