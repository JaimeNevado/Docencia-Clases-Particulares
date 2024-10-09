#include <iostream>

using namespace std;

int main()
{
	int array[] = {1, 2, 3, 4, 5};
	int *ptr = array;

	cout << array << endl;

	cout << ptr + 1 << endl; // 2
	cout << ptr + 2 << endl; // 3
	cout << ptr + 3 << endl; // 4
	cout << ptr + 4 << endl; // 5
	cout << ptr + 5 << endl; // F

	return 0;
}