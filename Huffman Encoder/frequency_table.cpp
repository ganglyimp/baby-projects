#include "frequency_table.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <exception>

frequency_table::frequency_table(const std::string &file_name) {
    std::ifstream file(file_name);
    
    if(!file) {
        throw std::runtime_error("File cannot be opened.");
    }
    else {
        char character;
        while(file.get(character)) {
            table[character]++;
        }

        file.close();
    }
}

frequency_table::~frequency_table() {}

int frequency_table::get_frequency(char c) const {
   if(table.find(c) == table.end())
        return 0;
   
   return table.at(c);
}