
#include<iostream>
#include "matrix.hpp"
using namespace std;

int main() {
    int rows, cols;
    std::cin >> rows >> cols;
    Matrix A(rows, cols);
    std::cin >> A;
    std::cin >> rows >> cols;
    Matrix B(rows, cols);
    std::cin >> B;
    std::cout << A * B;
    return 0;
}
// 失败了>..<