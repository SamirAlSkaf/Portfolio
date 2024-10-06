# Initialisierung des Dictionaries
table = {}

# Hinzufügen von Elementen
def add(key, value):
    table[key] = value

# Abrufen von Elementen
def get(key):
    return table.get(key)

# Ersetzen von Elementen
def replace(key, new_value):
    if key in table:
        table[key] = new_value
    else:
        print(f"Schlüssel '{key}' existiert nicht.")

# Entfernen von Elementen
def remove(key):
    table.pop(key, None)

# Überprüfen, ob ein Schlüssel existiert
def contains_key(key):
    return key in table

# Überprüfen auf Duplikate
def duplicate(key):
    return key in table

# Hauptfunktion
if __name__ == "__main__":
    # Elemente hinzufügen
    add("Name", "Alice")
    add("Alter", "25")

    # Elemente abrufen
    print("Name:", get("Name"))
    print("Alter:", get("Alter"))

    # Ersetzen von Elementen
    replace("Name", "Bob")
    print("Name nach Replace:", get("Name"))

    # Überprüfen auf Duplikate
    print("Hat Schlüssel 'Alter' Duplikate?", duplicate("Alter"))

    # Element entfernen
    remove("Name")
    print("Hat Schlüssel 'Name' nach Entfernen?", contains_key("Name"))
