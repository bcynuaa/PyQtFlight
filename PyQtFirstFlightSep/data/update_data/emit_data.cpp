/*
this file read data from `TestData.dat`
and emit data to `LatestData.dat`
the file shoud be overwrited each time
moreover, sensors are specified
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <iomanip>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iterator>
#include <map>
#include <set>
#include <utility>
#include <random>
#include <chrono>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <queue>
#include <functional>
#include <numeric>
#include <cassert>
#include <cstring>

std::string test_data_filename = "TestData.dat";
std::string emit_data_filename = "LatestData.dat";
std::string separator = "\t";
int emit_rows_each_time = 32;
int skiprows = 1;
float interval_second = 1.;

std::vector<std::vector<float>> readDataFromFile(std::string filename) {
    std::vector<std::vector<float>> data;
    std::string line;
    std::ifstream file(filename);
    if (file.is_open()) {
        int i = 0;
        while (std::getline(file, line)) {
            if (i < skiprows) {
                i++;
                continue;
            }
            std::vector<float> row;
            std::stringstream ss(line);
            float value;
            while (ss >> value) {
                row.push_back(value);
            }
            data.push_back(row);
        }
        file.close();
    }
    return data;
}


int emitDataEachTime(std::vector<std::vector<float>> data, int start_row) {
    // emit data to file
    // emit `emit_rows_each_time` rows
    // each row emit all data
    // after emit, wait for `interval_second` seconds
    // return 0 if success
    // return 1 if fail
    // morover the file should be overwrited each time
    std::ofstream file(emit_data_filename);
    if (file.is_open()) {
        for (int i = start_row; i < start_row + emit_rows_each_time; i++) {
            for (int j = 0; j < data[i].size(); j++) {
                file << data[i][j] << separator;
            }
            file << std::endl;
        }
        file.close();
        std::this_thread::sleep_for(std::chrono::milliseconds(int(interval_second * 1000)));
        return 0;
    }
    else {
        return 1;
    }
}

int emitDataLoop(std::vector<std::vector<float>> data) {
    // emit data loop
    // emit `emit_rows_each_time` rows each time
    // each row only emit `emit_columns_index` columns
    // after emit, wait for `interval_second` seconds
    // return 0 if success
    // return 1 if fail
    int start_row = 0;
    while (true) {
        if (start_row + emit_rows_each_time > data.size()) {
            start_row = 0;
        }
        int emit_result = emitDataEachTime(data, start_row);
        std::cout << "emit data from row " << start_row << " to row " << start_row + emit_rows_each_time << std::endl;
        if (emit_result == 0) {
            start_row += emit_rows_each_time;
        }
        else {
            return 1;
        }
    }
}

int main() {
    std::vector<std::vector<float>> data = readDataFromFile(test_data_filename);
    int emit_result = emitDataLoop(data);
    return emit_result;
}