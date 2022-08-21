"""

"""
from state_machine import acts_as_state_machine, State, Event, after, before


#@acts_as_state_machine
class Process():
    def __init__(self, names):
        self.name = names
    #define all the states of my state machine
        self.created = State(initial=True)
        self.waiting = State()
        self.running = State()
        self.terminated = State()
        self.blocked = State()
        self.swapped_out_waiting = State()
        swapped_out_blocked = State()
        # transitions
        self.wait = Event(from_state=(self.created, self.running, self.blocked,
                    self.swapped_out_waiting), to_state=self.waiting)

        # self.run = Event(from_state=waiting, to_state=running)

        # self.terminate = Event(from_state=running, to_state=terminated)

        # self.block = Event(from_state=running, to_state=blocked)

    # @after("wait")
    # def wait_info(self):
    #     print(f"{self.name} entered waiting mode ")

    # @after("run")
    # def run_info(self):
    #     print(f"{self.name} is running ")

    # @before("terminate")
    # def terminate_info(self):
    #     print(f"{self.name} is terminated")


p1, p2 = Process("p1"), Process("p2")
p1.wait()