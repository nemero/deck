from app.core.connection import Connection
from app.core.observer import Observer
from app.test_session import TestSession

if __name__ == "__main__":
	observer = Observer()
	connection = Connection(host="localhost", port=8080)

	connection.connect(observer)
	observer.register('message', 'system', 'info') # create observe event
	observer.register('test') # create observe event

	observer.subscribe('shutdown', connection.terminate) # the event will calling if server response command shutdown
	observer.subscribe('after-shutdown', connection.finish) # the event registered in connection class and calling when application will close

	test_session = TestSession()
	observer.subscribe('message', test_session.test)
	observer.subscribe('info', test_session.online)

	connection.run()