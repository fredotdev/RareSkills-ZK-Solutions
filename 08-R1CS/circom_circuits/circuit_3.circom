pragma circom 2.0.0;

template AddConstant() {
    signal input x;
    signal input y;
    signal output out;

    out <== x * y + 2;
 }

component main = AddConstant();
