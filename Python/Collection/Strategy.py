from abc import ABC, abstractmethod

# Strategie Interface
class IStrategy(ABC):
    @abstractmethod
    def execute(self):
        pass

# Konkrete Strategie A
class ConcreteStrategyA(IStrategy):
    def execute(self):
        print("Strategie A ausgeführt.")

# Konkrete Strategie B
class ConcreteStrategyB(IStrategy):
    def execute(self):
        print("Strategie B ausgeführt.")

# Kontext-Klasse
class Strategy:
    def __init__(self, strategy: IStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: IStrategy):
        self._strategy = strategy

    def execute_strategy(self):
        self._strategy.execute()

# Beispiel der Benutzung
if __name__ == "__main__":
    # Strategie-Objekt erstellen
    strategy_context = Strategy(ConcreteStrategyA())
    strategy_context.execute_strategy()  # Ausgabe: Strategie A ausgeführt.

    # Strategie zur Laufzeit ändern
    strategy_context.set_strategy(ConcreteStrategyB())
    strategy_context.execute_strategy()  # Ausgabe: Strategie B ausgeführt.
