#include "huffman_encoder.h"

huffman_encoder::huffman_encoder(const frequency_table &table){
    std::priority_queue<HeapNode*, std::vector<HeapNode*>, comp> minQueue;

    for(int i = 0; i < 128; i++) {
        char curr = i;
        int frequency = table.get_frequency(curr);

        if(frequency > 0) {
            HeapNode *thisNode = new HeapNode(curr, frequency, nullptr, nullptr); 

            minQueue.push(thisNode);
        }
    }
 
    while(minQueue.size() > 1) {
        HeapNode *left = minQueue.top();
        minQueue.pop();

        HeapNode *right = minQueue.top();
        minQueue.pop();

        int sum = left->freq + right->freq;
        HeapNode *empty = new HeapNode('\0', sum, left, right);
        minQueue.push(empty);
    }

    huffmanTree = minQueue.top();
    populateCodeTable("", huffmanTree);
}

huffman_encoder::~huffman_encoder() {
    destructorHelper(huffmanTree);
}

void huffman_encoder::destructorHelper(HeapNode *curr) {
    if(isLeaf(huffmanTree)) {
        huffmanTree = nullptr;
        delete curr;
    }
    else {
        if(isLeaf(curr)) {
            HeapNode *temp = curr;
            curr = huffmanTree;
            delete temp;
        }
        else {
            destructorHelper(curr->left);
            destructorHelper(curr->right);
        }
    }
}


std::string huffman_encoder::get_character_code(char character) const {
    if(codeTable.find(character) == codeTable.end())
        return "";
    else
        return codeTable.at(character);
}

std::string huffman_encoder::encode(const std::string &file_name) const {
    std::string encodedStr = "";

    std::ifstream file(file_name);

    if(!file) {
        throw std::runtime_error("File cannot be opened.");
    }
    else {
        char character;
        while(file.get(character)) {
            encodedStr += codeTable.at(character);
        }

        file.close();
    }
    
    return encodedStr;
}

std::string huffman_encoder::decode(const std::string &string_to_decode) const {
    std::string decodedStr = "";

    HeapNode *curr = huffmanTree;
    for(int i = 0; i < string_to_decode.size(); i++) {

        if(!isLeaf(curr)) {
            if(string_to_decode[i] == '0')
                curr = curr->left;
            else if(string_to_decode[i] == '1')
                curr = curr->right;
            else 
                return "";
        }

        if(isLeaf(curr)) {
            decodedStr += curr->c;
            curr = huffmanTree;
        }
    }
    
    return decodedStr;
}


void huffman_encoder::populateCodeTable(std::string code, HeapNode *current) {
    if(isLeaf(current)) {
        if(code == "")
            code = "0";

        codeTable[current->c] = code;
    }
    else {
        if(current->left) {
            populateCodeTable(code + "0", current->left);
        }
        
        if(current->right) {
            populateCodeTable(code + "1", current->right);
        }
    }
}

bool huffman_encoder::isLeaf(HeapNode *node) {
    return ((!node->left) && (!node->right));
}

bool huffman_encoder::isLeaf(HeapNode *node) const {
    return ((!node->left) && (!node->right));
}