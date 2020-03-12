#include <iostream>
using namespace std;

class XoFunc {
private:
	int n,m;
public:
	set_val(int,int);
	int compare() {
		if (n >= m) return (n/m);
		else return (m/n);
	}
};

XoFunc::set_val(int a,int b) {
	n = a;
	m = b;
}

int main (void) {
	XoFunc xo;
	xo.set_val(3,8);
	int i = xo.compare();
	while(i>0) {
		cout << "H";
		i--;
	}
	cout << endl;
	return 0;
}
