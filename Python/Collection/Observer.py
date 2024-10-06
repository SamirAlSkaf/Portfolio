# Der Beobachtbare (Subject)
class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify_observers()

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()

# Beobachter
class Observer:
    def __init__(self, name, subject):
        self._name = name
        self._subject = subject
        subject.attach(self)

    def update(self):
        print(f"{self._name} hat Update erhalten: {self._subject.state}")

# Hauptfunktion
if __name__ == "__main__":
    subject = Subject()

    observer1 = Observer("Beobachter 1", subject)
    observer2 = Observer("Beobachter 2", subject)

    subject.state = "Zustand 1"
    subject.state = "Zustand 2"

    subject.detach(observer1)

    subject.state = "Zustand 3"
