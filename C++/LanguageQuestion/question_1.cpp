/**
 * @file question_first.cpp
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2024-01-26
 * 
 * @copyright Copyright (c) 2024
 * 
 */
 /*
 编写一个 C++ 程序，其中包括一个带有私有 name（字符串）和 age（int）的 Person 类。
 实现一个参数化构造函数来初始化这些属性。添加一个成员函数 display，用于打印人的姓名和年龄。
 在主函数中，创建两个 Person 类实例，并使用 display 函数打印它们的信息。

 */

#include <iostream>
#include <string>
using namespace std;

class Person {

    public:
        // 参数化构造函数
        Person(const std::string& personName, int personAge) 
        : personName_m(personName), personAge_m(personAge)
        {}
    
        // 成员函数 display，用于打印姓名和年龄
        void display() const {
            cout<<personName_m<<" "<<personAge_m<<endl;
        }
    private:
        string personName_m;
        int personAge_m;
};

int main() {
    //实现你的功能
    Person someone1("Fufu",500);
    Person someone2("Hutao",16);
    someone1.display();
    someone2.display();
    return 0;
}