# prove knowledge of a solution to a linear system of equations.
# Can you generalize this to more variables?

# prove 10x + 7y = 142

from py_ecc.bn128 import G1, multiply, add

# Prover
secret_x = 10
secret_y = 6

x = multiply(G1, secret_x)
y = multiply(G1, secret_y)

proof = (x, y, 142)

# verifier
if multiply(G1, proof[2]) == add(multiply(proof[0], 10), multiply(proof[1], 7)):
    print("statement is true")
else:
    print("statement is false")