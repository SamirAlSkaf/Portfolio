#include <iostream>
#include <map>
#include <windows.h>
#include <mmsystem.h>

void playTone(int frequency) {
    Beep(frequency, 300);
}

int main() {
    std::map<char, int> keys = {
        {'c', 261}, // C
        {'v', 293}, // D
        {'b', 329}, // E
        {'n', 349}, // F
        {'m', 392}  // G
    };

    std::cout << "Drücke Tasten (c, v, b, n, m) für Töne. Drücke ESC zum Beenden." << std::endl;

    while (true) {
        if (GetAsyncKeyState(VK_ESCAPE)) break;

        for (const auto& [key, frequency] : keys) {
            if (GetAsyncKeyState(key)) {
                playTone(frequency);
                Sleep(100); // Kurze Pause
            }
        }
    }

    return 0;
}
