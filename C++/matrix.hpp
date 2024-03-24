/**
 * 完善 Matrix 类，使得下面的代码可以正常运行:
 * class Matrix {
 * public:
 * TODO: Someting
 * private:
 *     int rows;
 *     int cols;
 *     int **matrix;
 * };
 *
 * 评分标准：
 * 1. 代码能够正常的运行就有 100 分，若代码不能正常运行，则按以下标准进行评分：
 * Matrix::Matrix(int rows, int cols):                              20 points
 * Matrix::~Matrix():                                               20 points
 * std::istream& operator>>(std::istream& in, Matrix& matrix)       20 points
 * std::ostream& operator<<(std::ostream& os, const Matrix& matrix) 20 points
 * Matrix Matrix::operator*(Matrix &other)                          20 points
 * 2. 在正常运行的基础上，若还有其他的功能，则按以下标准进行评分：
 * Matrix::Matrix(int rows, int cols, int** matrix)                 10 points
 * template <size_t rows, size_t cols> Matrix::Matrix(int (&matrix)[rows][cols])        10 points
 * Matrix::Matrix(const Matrix& other)                              10 points
 * Matrix::Matrix(Matrix&& other)                                   10 points
 * Matrix& Matrix::operator=(const Matrix& other)                   10 points
 * Matrix& Matrix::operator=(Matrix &&other)                        10 points
 * Matrix Matrix::operator+(const Matrix& other)                    10 points
 * Matrix Matrix::operator-(const Matrix& other)                    10 points
 * Matrix Matrix::operator/(const Matrix& other)                    10 points
 * bool Matrix::operator==(const Matrix& other)                     10 points
 */
#include<iostream>

class Matrix {
public:
    Matrix(int rows, int cols):rows(rows),cols(cols) {}
    ~Matrix(){
        // 释放二维数组内存
        for (int i = 0; i < rows; ++i) {
            delete[] matrix[i];
        }
        delete[] matrix;
    }
    friend std::istream& operator>>(std::istream& in, Matrix& matrix);
    friend std::ostream& operator<<(std::ostream& os, const Matrix& matrix);
    friend Matrix operator*(const Matrix& a, const Matrix& b);
  
private:
    int rows;
    int cols;
    int **matrix;
};
std::istream& operator>>(std::istream& in, Matrix& matrix){
    for(int i=0;i<matrix.rows;++i){
        for(int j=0;j<matrix.cols;++j){
            in >> matrix.matrix[i][j];
        }
    }
    return in;
}
std::ostream& operator<<(std::ostream& os, const Matrix& matrix) {
    for (int i = 0; i < matrix.rows; ++i) {
        for (int j = 0; j < matrix.cols; ++j) {
            os << matrix.matrix[i][j] << ' ';
        }
        os << '\n';
    }
    return os;
}
Matrix operator*(const Matrix& a, const Matrix& b) {
    if (a.cols != b.rows) {
        throw std::invalid_argument("Matrices dimensions do not match for multiplication.");
    }

    Matrix result(a.rows, b.cols);

    for (int i = 0; i < a.rows; ++i) {
        for (int j = 0; j < b.cols; ++j) {
            for (int k = 0; k < a.cols; ++k) {
                result.matrix[i][j] += a.matrix[i][k] * b.matrix[k][j];
            }
        }
    }
    return result;
}