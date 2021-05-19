/**
 * @file camelCase.cpp
 * @author Sayantan Paul
 * @brief CamelCase
 */

#include <iostream>
#include <string>

int main() {
    std::string str;
    std::cin >> str;
    int count = 1;
    for (int i = 1; i < str.length(); i++)
    {
        if (str.at(i) >= 'A' && str.at(i) <= 'Z') count++;
    }
    
    std::cout << "Number of words: " << count << std::endl;
}