import asyncio

# Hauptfunktion, die asynchrone Aufgaben ausführt
async def run_async():
    print("Start der asynchronen Methoden")

    # Zwei Aufgaben parallel starten
    task1 = asyncio.create_task(task1_async())
    task2 = asyncio.create_task(task2_async())

    # Warten, bis beide Aufgaben fertig sind
    await asyncio.gather(task1, task2)

    print("Ende der asynchronen Methoden")

# Erste asynchrone Aufgabe
async def task1_async():
    print("Task1 gestartet")
    await asyncio.sleep(2)  # 2 Sekunden warten
    print("Task1 beendet")

# Zweite asynchrone Aufgabe
async def task2_async():
    print("Task2 gestartet")
    await asyncio.sleep(3)  # 3 Sekunden warten
    print("Task2 beendet")

# Die asynchrone Hauptfunktion ausführen
asyncio.run(run_async())
