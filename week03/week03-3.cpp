#include <iostream>
#include <string>
using namespace std; /// �R�W
int main()
{
    string s;
    cout << "�п�J�@�ӫܪ����r��,�������n���Ů�: ";
    cin >> s;
    cout << "�r��" << s << "�����׬O" << s.length() << "\n";
    for(int i=0;i<s.length(); i++){
        cout << i << ":" << s[i] << endl; /// endl �p�gL �N�O"\n"
    }
}
