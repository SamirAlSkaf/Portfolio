#include <iostream>
#include <unordered_map>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

const double EARTH_RADIUS = 6371.0;

struct City {
    double latitude;
    double longitude;
};

unordered_map<string, City> cities = {
    {"berlin", {52.5200, 13.4050}},
    {"paris", {48.8566, 2.3522}},
    {"madrid", {40.4168, -3.7038}},
    {"rome", {41.9028, 12.4964}},
    {"london", {51.5074, -0.1278}},
    {"amsterdam", {52.3676, 4.9041}},
    {"brussels", {50.8503, 4.3517}},
    {"vienna", {48.2082, 16.3738}},
    {"prague", {50.0755, 14.4378}},
    {"copenhagen", {55.6761, 12.5683}},
    {"stockholm", {59.3293, 18.0686}},
    {"helsinki", {60.1695, 24.9354}},
    {"budapest", {47.4979, 19.0402}},
    {"zagreb", {45.8150, 15.9819}},
    {"sarajevo", {43.8486, 18.3564}},
    {"belgrade", {44.7866, 20.4489}},
    {"sofia", {42.6977, 23.3219}},
    {"tirana", {41.3275, 19.8189}},
    {"skopje", {41.9973, 21.4280}},
    {"pristina", {42.6629, 21.1655}},
    {"tbilisi", {41.7151, 44.8271}},
    {"yerevan", {40.1792, 44.4991}},
};

double toRadians(double degree) {
    return degree * M_PI / 180.0;
}

double calculateDistance(City city1, City city2) {
    double lat1 = toRadians(city1.latitude);
    double lat2 = toRadians(city2.latitude);
    double deltaLat = toRadians(city2.latitude - city1.latitude);
    double deltaLon = toRadians(city2.longitude - city1.longitude);

    double a = sin(deltaLat / 2) * sin(deltaLat / 2) +
               cos(lat1) * cos(lat2) *
               sin(deltaLon / 2) * sin(deltaLon / 2);
    double c = 2 * atan2(sqrt(a), sqrt(1 - a));

    return EARTH_RADIUS * c;
}

string toLowerCase(const string& str) {
    string lowerStr = str;
    transform(lowerStr.begin(), lowerStr.end(), lowerStr.begin(), ::tolower);
    return lowerStr;
}

int main() {
    string city1, city2;

    cout << "Choose your first European capital city: ";
    getline(cin, city1);
    cout << "Choose your second European capital city: ";
    getline(cin, city2);

    city1 = toLowerCase(city1);
    city2 = toLowerCase(city2);

    if (cities.find(city1) == cities.end() || cities.find(city2) == cities.end()) {
        cout << "Error: One or both cities are invalid." << endl;
        return 1;
    }

    double distance = calculateDistance(cities[city1], cities[city2]);
    cout << "The distance between " << city1 << " and " << city2 << " is " << distance << " km." << endl;

    return 0;
}
