from Observer import Observer
class Observable:
    def __init__(self):
        self._observers: list[Observer] = [ ]
    
    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            print("The given observer doesn't exist")
    
    def notify(self, observer):
       observer.update(self) 

    def notify_all(self):
        for observer in self._observers:
            observer.update(self)
