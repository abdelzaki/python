"""
State machine: it consists of state and transition  

State pattern : encapsulate states in seperate state classes 
    Context : it has the method to modify the interal state 
    State interface : allow context to communicate with the different state 
    Concrete states : each state is reprensed by the concrete state 

    doSomething in the context is implemented according to the active state 
"""
from abc import ABC, abstractmethod, abstractproperty
from enum import IntEnum
from tkinter.messagebox import NO


def simpleState():
    State = IntEnum("State", "ON OFF")

    class SimpleState():
        def __init__(self) -> None:
            self._state: State = State.OFF

        def onOF(self, switch: State):
            if switch == State.ON:
                self._state = State.ON
            if switch == State.OFF:
                self._state = State.OFF

    simpleState = SimpleState()
    simpleState.onOF(State.ON)
    print(int(simpleState._state))
    simpleState.onOF(State.OFF)
    print(int(simpleState._state))


class Context:
    def __init__(self, state) -> None:
        self.setState(state)

    def setState(self, state):
        self._state = state
        self._state.context = self

    def doSomething(self):
        self._state.doSomething()


class AbstractState(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.context: Context = None

    @abstractmethod
    def doSomething():
        pass


class ConcreateStateA(AbstractState):
    def doSomething(self):
        print(" the context is in state A ")
        self.context.setState(ConcreateStateB())


class ConcreateStateB(AbstractState):
    def doSomething(self):
        print(" the context is in state B ")
        self.context.setState(ConcreateStateA())


context = Context(ConcreateStateA())
context.doSomething()
context.doSomething()
context.doSomething()

""""""
