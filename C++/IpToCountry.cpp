#include <iostream>
#include <string>
#include <geoip2/geoip2.hpp>

using namespace std;

string getCountryFromIP(const string& ip) {
    try {
        geoip2::Reader reader("GeoLite2-Country.mmdb");
        auto response = reader.country(ip);
        return response.country.iso_code;
    } catch (const geoip2::GeoIP2Error& e) {
        return "Country not found";
    } catch (const std::exception& e) {
        return "Invalid IP format";
    }
}

int main() {
    string ip;
    cout << "Enter an IP address to find the corresponding country: ";
    getline(cin, ip);
    
    string country = getCountryFromIP(ip);
    cout << "Country: " << country << endl;

    return 0;
}
