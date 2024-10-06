class MyClass:
    def __init__(self, value):
        self.value = value

# Erhalten der Singleton-Instanz
instance1 = get_instance(MyClass, 42)
instance2 = get_instance(MyClass, 99)

print(instance1.value)  # Ausgabe: 42
print(instance2.value)  # Ausgabe: 42 (beide Instanzen sind gleich)
