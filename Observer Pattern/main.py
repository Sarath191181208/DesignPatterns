from Observer import Observer
from Observable import Observable

class Publisher(Observable):
    def __init__(self, data: int) -> None:
        self._data: int = data
        Observable.__init__(self)
    
    @property
    def data(self) -> None:
        return self._data

    @data.setter
    def data(self, value: int) -> None:
        self._data = value
        self.notify_all()

class Subscriber(Observer):
    def __init__(self, name: str) -> None:
        self._name = name

    def update(self, newObservable: Observable, *args, **kwargs):
        val: int = newObservable.data
        print(f"{self._name} updated with the {val= } ")

def main() -> None:
    sub_1 = Subscriber("1")
    sub_2 = Subscriber("2")
    sub_3 = Subscriber("3")

    subject = Publisher(0)

    subject.add_observer(sub_1)
    subject.add_observer(sub_2)
    subject.add_observer(sub_3)

    subject.data = 4

    print("---"*20)
    print("Update to 4 completed !")
    print("---"*20)
    
    subject.data = 5

    print("Updates completed")

if __name__ == "__main__":
    main()

