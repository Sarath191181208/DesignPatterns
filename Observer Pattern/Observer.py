from abc import ABC

class Observer(ABC):
    def update(self, observable_object, *args, **kwargs):
        """updates the state of the observer"""
