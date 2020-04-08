#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <algorithm>

typedef std::vector<std::string> WordVec;

// Get all the words from a file and return a vector with said words.
WordVec getWordsFromFile(const std::string &file = "/usr/share/dict/words") {
    WordVec words;

    std::ifstream readFile(file);
   
    if (readFile.is_open()) {
        std::string line;
        while(getline (readFile, line)) {
            words.push_back(line);
        }

        readFile.close();
    }

    return words;
}

WordVec getRandomWords(const size_t number, const std::string &file = "/usr/share/dict/words") {
    // Get words from given file
    WordVec words = getWordsFromFile(file);
    WordVec randomWords;

    std::sample(words.begin(), words.end(), std::back_inserter(randomWords), number, std::mt19937{std::random_device{}()});

    return randomWords;
}

std::string getRandomWord(const std::string &file = "/usr/share/dict/words") {
    WordVec words = getRandomWords(1, file);

    // return the 1 sampled word
    return words.at(0);
}

void print(WordVec const &input) {
    for (size_t i = 0; i < input.size(); i++) {
        std::cout << input.at(i) << " ";
    }
}

int main() {
    WordVec words = getWordsFromFile();
    WordVec randomWords = getRandomWords(10);
    std::string singleWord = getRandomWord();

    print(randomWords);
    std::cout << "\n" << singleWord; 

    return 0;
}
