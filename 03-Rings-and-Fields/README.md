# Rings and Fields
## Solutions
### by a ring’s definition, why is the above statement not always true? What assumption is it making about the ring?
That the second operator is commutative
### use the definition of a ring to show that the trivial ring is in fact a ring
- {0} under addition is abelian because:
	- 0 + 0 = 0 is closed
	- 0 + 0 = 0 + 0 is commutative
	- 0 + (0 + 0) = (0 + 0) + 0 is associative
	- 0 is the inverse element
	- 0 is the identity element
- {0} under multiplication is monoid because it is:
	- Magma: because it is closed 0 * 0 = 0, which is in {0}
	- Semigroup: because the operator is associative  0 * (0 * 0) = (0 * 0) * 0
	- Monoid: because 0 is the identity element (not really)
- Distributive property
	- (a + b) * c = (a * c) + (b * c)
	- c * (a + b) = (c * a) + (c * b)
### Square matrices of real numbers under addition and multiplication is a ring. Demonstrate this to be the case. Think carefully about what the identity elements are and whether an inverse always exists.
- Square matrix under addition is abelian because:
	- addition is closed (adding square matrices gives a square matrix)
	- addition is commutative
	- addition is associative
	- negative matrix is the inverse element
	- zero matrix is the identity element
- Square matrix under multiplication is monoid because:
	- multiplication is closed (multiplying square matrices gives a square matrix)
	- multiplication is associative
	- identity element is the identity matrix (zero's everywhere except 1's on the diagonal)
- distributive property: same as above
### It isn’t possible to construct a trivial field using one element. Why is that the case? Hint: how many identity elements are needed? Hint: remember, the definition of a field is that the zero element is removed. An empty set cannot be a group.
A field requires 2 distinct identity elements, 0 for addition and 1 for multiplication