#include <iostream>
using namespace std;

///struct Node {}; /// ������������ C�y�����c
///class Cat{}; ///���e�X�g�A���йLC++��j�j
struct Node {
    int val; /// value�Y�g�A�o��Node�̭�����
};
class Cat{
public:
    string name; ///�ߪ��W�r�A���e�X�g�йL
};
int main()
{
    Cat cat1;
    cat1.name = "cattie";
    Node node;
    node.val = 1;
}