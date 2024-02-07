# prove knowledge of a solution to a linear system of equations.
# Can you prove you know x such that 23x = 161?

from py_ecc.bn128 import G1, multiply, add

# Prover
secret_x = 7

x = multiply(G1, secret_x)

proof = (x, 161)

# verifier
if multiply(G1, proof[1]) == multiply(proof[0], 23):
    print("statement is true")
else:
    print("statement is false")