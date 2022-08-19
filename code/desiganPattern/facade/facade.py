"""
The façade design pattern helps us to hide the internal complexity of our systems and
expose only what is necessary to the client through a simplified interface provide a single entery point 
"""

from enum import Enum
import abc

State = Enum("State", "new running sleeping restart zombie")


class Server(abc.ABC):
    @abc.abstractmethod
    def boot(self):
        pass

    @abc.abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):
    def __init__(self) -> None:
        self.name = "File server"
        self.state = State.new

    def boot(self):
        print(f"Booting {self.name}")
        self.state = State.running

    def kill(self, restart=True):
        print(f"Stop the server {self.name}")

        self.state = State.restart

    def createFile(self):
        print(f"File is created from {self.name}")


class ProcessServer(Server):
    def __init__(self) -> None:
        self.name = "Process server"
        self.state = State.new

    def boot(self):
        print(f"Booting {self.name}")
        self.state = State.running

    def kill(self, restart=True):
        print(f"Stop the server {self.name}")

        self.state = State.restart

    def createProcess(self):
        print(f"Process is created from {self.name}")


class OperatingSystem:
    '''The Facade'''

    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)
