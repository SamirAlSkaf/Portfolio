import threading
import time

# Funktion, die von den Threads ausgeführt wird
def do_work():
    for i in range(5):
        print(f"Thread {threading.get_ident()} ist am Arbeiten.")
        time.sleep(1)  # Simuliere Arbeit

# Hauptfunktion
def main():
    # Erstelle und starte zwei Threads
    thread1 = threading.Thread(target=do_work)
    thread2 = threading.Thread(target=do_work)

    thread1.start()
    thread2.start()

    # Warte, bis beide Threads beendet sind
    thread1.join()
    thread2.join()

    # Ausgabe nach Abschluss beider Threads
    print("Beide Threads sind beendet.")

# Ausführen der main-Funktion
if __name__ == "__main__":
    main()
