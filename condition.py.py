import socket
def create():
   try:
    socket.create_connection(("8.8.8.8",53))
    return True
   except OSError:
    return False
status="up" if create() else "down"
print(status)
import datetime
dt=datetime.datetime.now()
print(dt.strftime("%I:%M"))
