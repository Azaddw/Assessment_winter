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

