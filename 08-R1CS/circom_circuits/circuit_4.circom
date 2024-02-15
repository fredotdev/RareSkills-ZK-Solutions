pragma circom 2.0.0;

template MultiplyConstant() {
    signal input x;
    signal input y;

    signal v1;

    signal output out;

    v1 <== x * x;

    out <== 2 * v1 + y;
 }

component main = MultiplyConstant();