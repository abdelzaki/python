"""
u pass the data to each node where each node make a change to the data and then pass
it to the next node
"""
import abc


class Event:
    """it represent the data which we should process"""

    def __init__(self, name: str) -> None:
        self.name: str = name

    def __str__(self) -> str:
        return self.name


class Widget(abc.ABC):
    """here we can implement dispatcher to decide which function 
    according to the name of the event which is so good idea """
    @abc.abstractmethod
    def __init__(self, parent=None) -> None:
        self.parent = parent

    def handle(self, event: Event):
        """this method implement command dispatcher """
        handler = f"handle_{event}"
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        if self.parent is not None:
            self.parent.handle(event)


class MainWindow(Widget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
    """Here we implement a specific handle_"""

    def handle_close(self, event: Event):
        print(f"MainWindow handle {event}")


class SendDialog(Widget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

    def handle_close(self, event: Event):
        print(f"SendDialog handle {event}")


eventClosed = Event("close")
mainWindow = MainWindow()

sendDialog = SendDialog(mainWindow)
sendDialog.handle(eventClosed)
