#pragma once

#include "frequency_table.h"
#include <vector>
#include <queue>
#include <algorithm>
#include <unordered_map>
#include <iostream>
#include <fstream>
#include <sstream>
#include <exception>

struct HeapNode {
    char c;
    int freq;
    HeapNode *left;
    HeapNode *right;

    HeapNode(char ch, int f, HeapNode *l, HeapNode *r): c(ch), freq(f), left(l), right(r) {}
};

struct comp {
    bool operator()(HeapNode *l, HeapNode *r) {
        return (l->freq) > (r->freq);
    }
};

class huffman_encoder {
    public:
        huffman_encoder(const frequency_table &table);
        ~huffman_encoder();
        void destructorHelper(HeapNode *curr);

        std::string get_character_code(char c) const;
        std::string encode(const std::string &file_name) const;
        std::string decode(const std::string &file_name) const;

        void populateCodeTable(std::string code, HeapNode *current);
        bool isLeaf(HeapNode *node);
        bool isLeaf(HeapNode *node) const;

        std::unordered_map<char, std::string> codeTable;
        HeapNode *huffmanTree;
};