/**
 * @file exploreMars.cpp
 * @author Sayantan Paul
 * @brief Mars Exploration
 */

#include <iostream>
#include <string>

int exploreMars(std::string);

int main() {
    std::cout << "SOS: " << exploreMars("SOS") << std::endl;
    std::cout << "SQS: " << exploreMars("SQS") << std::endl;
    std::cout << "SQR: " << exploreMars("SQR") << std::endl;
    std::cout << "QQS: " << exploreMars("QQS") << std::endl;
    std::cout << "QQR: " << exploreMars("QQR") << std::endl;
    return 0;
}

/**
 * @brief function to take input string and find number of replacements required for a correct sos message
 * 
 * @param input : distorted sos-string
 * @return int : number of corrections required
 */
int exploreMars(std::string input) {
    int count = 0;

    for (unsigned i = 0; i < input.length(); i+=3) {
        if (input.at(i) != 'S') count++;
        if (input.at(i + 1) != 'O') count++;
        if (input.at(i + 2) != 'S') count++;
    }

    return count;
}