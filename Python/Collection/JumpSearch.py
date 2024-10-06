import math

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Finden des Blocks, in dem das Element sein könnte
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Lineare Suche im gefundenen Block
    for i in range(prev, min(step, n)):
        if arr[i] == x:
            return i

    return -1

# Hauptfunktion
def main():
    arr = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]
    x = 19  # Wert, den wir suchen

    result = jump_search(arr, x)

    if result != -1:
        print(f"Element {x} gefunden an Index {result}")
    else:
        print(f"Element {x} nicht gefunden")

# Ausführen der main-Funktion
main()
