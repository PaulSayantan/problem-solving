/**
 * @file halloweenSale.cpp
 * @author Sayantan Paul
 * @brief Halloween Sale
 */

#include <iostream>
#include <vector>
#include <string>

int how_many_games(int, int, int, int);

int main() {
    int p, d, m, s;
    std::cin >> p >> d >> m >> s;

    std::cout << "Number of games bought: " << how_many_games(p, d, m, s);
}

int how_many_games(int p, int d, int m, int s) {
    int count = 0, sum = 0;

    while (p >= m) {
        sum += p;
        if (sum > s)
            break;
        count++;
        if (p - d > m)
            p = p - d;
        else
            p = m;
    }

    return count;
}