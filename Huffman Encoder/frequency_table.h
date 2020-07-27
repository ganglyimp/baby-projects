#pragma once

#include <iostream>
#include <unordered_map> 

class frequency_table {
    std::unordered_map<char, int> table;

    public:
        frequency_table(const std::string &file_name);
        ~frequency_table();
        
        int get_frequency(char c) const;
};