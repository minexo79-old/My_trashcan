#include <iostream>
using namespace std;

class Xofunc {
private:
    int n;
public:
    input_value(int);
    int xopow(void) {
        if((n%2 == 0 && n%3 == 0) || n%3 == 0)
            return n*n*n;
        else
            return n*n;        
    }
    int discri_max(int v[3]) {
        int i,max=0;
        for(i=0;i<3;i++) {
            if(v[i] >= max)
                max = v[i];
        }
        return max;     
    }
};

Xofunc::input_value(int val) {
    n = val;
}

int main () {
    Xofunc xo;
    int a[3]={8,12,14},i,newa[3],result;
    for(i=0;i<3;i++) {
        xo.input_value(a[i]);
        newa[i] = xo.xopow();
    }
    result = xo.discri_max(newa);
    cout << result << endl;
    return 0;
}