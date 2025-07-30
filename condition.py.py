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
def mathematics():
    a=int(input(any))
    b=int(input(any))
    c=input("symbol")
    if c=="/": print(a/b)
    elif c=="x": print(f"{a}x{b}={a*b}")
    elif c=="+": print(a+b)
    elif c=="-": print(a-b)
    else: 
        print("define what to do")
        pass
