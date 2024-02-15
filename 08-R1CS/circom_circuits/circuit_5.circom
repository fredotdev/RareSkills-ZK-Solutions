pragma circom 2.0.0;

template Polynomial() {
    signal input x;
    signal input y;
    
    signal v1;
    signal v2;
    
    signal output out;
    
    v1 <== x * x;
    v2 <== v1 * y;
    
    out <== 3*v2 + 5 * x * y-x - 2*y + 3;
}

component main = Polynomial();