# Group 8 - Group Work 1
## Project:

Build a trivial date server and client, illustrating simple one-way
communication. The server sends data to the client only.

-----

because the course actually focuses on using low-level network programming, and not frameworks,
we will use sockets for the project

The notes use java, but i don't think many of us are conversant, or can get conversant with it because of hoe verbose it is
for that reason, we will use python for our server and client codes

---

### project structure
the server code is lovcated in ./server.py, and the client code is in ./client.py


----

plese do not push directly to the main(develop) branch

rather, create your own git branch that has your name, push to it and create a pull request so i review the code and perform what magical fusion has to be done




the goal of the project is this:

we have server.py run with: 
```bash
 python server.py

```

and have client.py run with: 
```bash
python client.py

```

server code:
create a listening socket that runs indefinitely as the process is running
when another socket connects to this (i.e the client), the server uses the datetime module to send the current date to the connected client

client code:
creates a connecting socket
when the process starts running, it connects to the server socket, receives the date, then disconnects without sending a response.
the client should never send data to the server, or request for data. it only connects (hence achieving one-way communication).
It outputs the date received from the server, then ends the program


to take thsi to a more advanced level, 
we can 
 - use multithreading to allow the server handle multiple clients on separate threads, 
 - or use asyncio to have everything run via co-routines


but let use start with this simple version
i will provide some boilerplate code in the develop branch
