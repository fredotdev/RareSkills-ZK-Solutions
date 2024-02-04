##### Assume you have a proper definition for integers. Create a well-defined set of rational numbers.
$$\mathbb{Q}=\lbrace \frac{a}{b} \vert a, b\in\mathbb{Z}, b \neq 0 \rbrace$$
###### Define the subset relationship between integers, rational numbers, real numbers, and complex numbers.
$$\mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$$
###### Define the relationship between the set of transcendental numbers and the set of complex numbers in terms of subsets. Is it a proper subset?
$$\text{transcenental numbers} \subset \mathbb{C}$$
###### Using the formal definition of equality, show that if two finite sets have different cardinality, they cannot be equal. (Demonstrating this for infinite sets is a little trickier, so we skip that).
$$\text{definition: } A = B \leftrightarrow A \subseteq B \text{ and } B \subseteq A$$
$$\text{Let's say } A = B \text{ and } \lvert A \rvert < \lvert B \rvert$$
$$B \subseteq A \text{ impossible } \rightarrow \text{contradiction}$$
$$\text{Same for } \lvert A \rvert > \lvert B \rvert$$
###### Compute the cartesian product of B × A using the definitions above.
|  | x | y | z |
| ---- | ---- | ---- | ---- |
| 1 | (x, 1) | (y, 1) | (z, 1) |
| 2 | (x, 2) | (y, 2) | (z, 2) |
| 3 | (x, 3) | (y, 3) | (z, 3) |
{(x, 1), (x, 2), (x, 3), (y, 1), (y, 2), (y, 3), (z, 1), (z, 2), (z, 3)}
##### Compute the cartesian product of {1,2,3,4} and {3,6,9,12} (in that order). If you were to pick 4 particular ordered pairs from this, what arithmetic computation would that encode?
|     | 1       | 2       | 3       | 4       |
| --- | ------- | ------- | ------- | ------- |
| 3   | (1, 3)  | (2, 3)  | (3, 3)  | (4, 3)  |
| 6   | (1, 6)  | (2, 6)  | (3, 6)  | (4, 6)  |
| 9   | (1, 9)  | (2, 9)  | (3, 9)  | (4, 9)  |
| 12  | (1, 12) | (2, 12) | (3, 12) | (4, 12) |
##### Define a mapping (function) from integers n ∈ 1,2,3,4,5,6 to the set {even, odd}.
|      | 1   | 2   | 3   | 4   | 5   | 6   |
| ---- | --- | --- | --- | --- | --- | --- |
| even | x    | (2, even)    | x    | (4, even)    | x    | (6, even)    |
| odd     | (1, odd)    | x    | (3, odd)    | x    | (5, odd)    | x    |
##### Take the cartesian product of the set of integers 0,1,2,…,8 and the polygons triangle, square, pentagon, hexagon, heptagon, and octagon. Define a mapping such that the integer maps to the number of sides on the shape. For example, the ordered pair (4, □) should be in the subset, but (7,△) should not be in the subset of the cartesian product.
|          | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| triangle |     |     |     | (3, △)    |     |     |     |     |     |
| square   |     |     |     |     | (4, □)    |     |     |     |     |
| pentagon |     |     |     |     |     | (5, ⬠)    |     |     |     |
| hexagon  |     |     |     |     |     |     | (6, ⬡)    |     |     |
| heptagon |     |     |     |     |     |     |     | (7, heptagon)    |     |
| octagon         |     |     |     |     |     |     |     |     | (8, octagon)    |
##### Define a mapping between positive integers and positive rational numbers (not the whole thing, obviously). It is possible to perfectly map the integers to rational numbers. Hint: draw a table to construct rational numbers where the columns are the numerators and the rows are the denominators. Struggle with this for at least 15 minutes before looking up the answer.
reduced table:

|  | 1 | 2 | 3 | 4 | 5 | ... |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | $\frac{1}{1}$ | $\frac{2}{1}$ | $\frac{3}{1}$ | $\frac{4}{1}$ | $\frac{5}{1}$ |  |
| 2 | $\frac{1}{2}$ |  | $\frac{3}{2}$ |  | $\frac{5}{2}$ |  |
| 3 | $\frac{1}{3}$ | $\frac{2}{3}$ |  | $\frac{4}{3}$ | $\frac{5}{3}$ |  |
| 4 | $\frac{1}{4}$ |  | $\frac{3}{4}$ |  | $\frac{5}{4}$ |  |
| 5 | $\frac{1}{5}$ | $\frac{2}{5}$ | $\frac{3}{5}$ | $\frac{4}{5}$ |  |  |
| ... |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
mapping (cantor diagonal argument):

| integer | rational number |
| ------- | --------------- |
| 1       | $\frac{1}{1}$   |
| 2       | $\frac{1}{2}$   |
| 3       | $\frac{2}{1}$   |
| 4       | $\frac{1}{3}$   |
| 5       | $\frac{3}{1}$   |
| 6       | $\frac{1}{4}$   |
| 7       | $\frac{2}{3}$   |
| 8       | $\frac{3}{2}$   |
| 9       | $\frac{4}{1}$   |
| 10      | $\frac{1}{5}$   |
| 11      | $\frac{5}{1}$   |
| ...        | ...                |
##### Let set A be {1,2,3} and set B be {x,y,z}. Define a function from A to B that is well-defined, but not surjective and not injective.
$1 \rightarrow x$
$2 \rightarrow x$
$3 \rightarrow x$
##### Pick a subset of ordered pairs that defines a * b mod 3.
|  | (0,0) | (1,0) | (2,0) | (0,1) | (1,1) | (2,1) | (0,2) | (1,2) | (2,2) |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0 | ((0,0), 0) | ((1,0), 0) | ((2,0), 0) | ((0,1), 0) |  |  | ((0,2), 0) |  |  |
| 1 |  |  |  |  | ((1,1), 1) |  |  |  | ((2,2), 1) |
| 2 |  |  |  |  |  | ((2,1), 2) |  | ((1,2), 2) |  |
##### Demonstrate the above statement is correct by reasoning from ((a, b), c) and ((b, a), c) and the definition of injective.
(Here is an interesting fact about the relation between (A x A) and A (shown in the final table above): if the binary operator is commutative, then the map from (A x A) to A cannot be injective if the cardinality of the set is 2 or greater.)

|  | (a,a) | (b,a) | (c,a) | (a,b) | (b,b) | (c,b) | (a,c) | (b,c) | (c,c) |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| a |  |  |  |  |  |  |  |  |  |
| b |  |  |  |  |  |  |  |  |  |
| c |  | ((b,a), c) |  | ((a,b), c) |  |  |  |  |  |
$c \rightarrow (b,a)$
$c \rightarrow (a,b)$
##### Define our set A to be the numbers 0,1,2,3,4 and our binary operator to be subtraction modulo 5. Define all the ordered pairs of A ⨉ A in a table, then map that set of ordered pairs to A.
|  | 0 | 1 | 2 | 3 | 4 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 0 | (0,0) | (1,0) | (2,0) | (3,0) | (4,0) |
| 1 | (0,1) | (1,1) | (2,1) | (3,1) | (4,1) |
| 2 | (0,2) | (1,2) | (2,2) | (3,2) | (4,2) |
| 3 | (0,3) | (1,3) | (2,3) | (3,3) | (4,3) |
| 4 | (0,4) | (1,4) | (2,4) | (3,4) | (4,4) |

|  | (0,0) | (1,0) | (2,0) | (3,0) | (4,0) | (0,1) | (1,1) | (2,1) | (3,1) | (4,1) | (0,2) | (1,2) | (2,2) | (3,2) | (4,2) | (0,3) | (1,3) | (2,3) | (3,3) | (4,3) | (0,4) | (1,4) | (2,4) | (3,4) | (4,4) |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0 | ((0,0), 0) |  |  |  |  |  | ((1,1), 0) |  |  |  |  |  | ((2,2), 0) |  |  |  |  |  | ((3,3), 0) |  |  |  |  |  | ((4,4), 0) |
| 1 |  | ((1,0), 1) |  |  |  |  |  | ((2,1), 1) |  |  |  |  |  | ((3,2), 1) |  |  |  |  |  | ((4,3), 1) | ((0,4), 1) |  |  |  |  |
| 2 |  |  | ((2,0), 2) |  |  |  |  |  | ((3,1), 2) |  |  |  |  |  | ((4,2), 2) | ((0,3), 2) |  |  |  |  |  | ((1,4), 2) |  |  |  |
| 3 |  |  |  | ((3,0), 3) |  |  |  |  |  | ((4,1), 3) | ((0,2), 3) |  |  |  |  |  | ((1,3), 3) |  |  |  |  |  | ((2,4), 3) |  |  |
| 4 |  |  |  |  | ((4,0), 4) | ((0,1), 4) |  |  |  |  |  | ((1,2), 4) |  |  |  |  |  | ((2,3), 4) |  |  |  |  |  | ((3,4), 4) |  |
##### Work out for yourself that concatenating “foo”, “bar”, “baz” in that order is associative. Remember, associative means (A op B) op C = A op (B op C).
(foo + bar) + baz = foobar + baz = foobarbaz = foo + barbaz = foo + (bar + baz)
##### Give an example of a magma and a semigroup. The magma must not be a semigroup. Don’t use the examples above.
magma: integer subtraction
semigroup: integer multiplication
##### Let our binary operator be the function min(a,b) over integers. Is this a magma, semigroup, or monoid? What if we restrict the domain to be positive integers (zero or greater)? What about the binary operator max(a,b) over those two domains?
**min(a,b) integers:** semigroup
**min(a, b) positive integers:** semigroup
**max(a, b) integers:** semigroup
**max(a, b) positive integers:** monoid
##### Let our set be all 3 bit binary numbers (a set of cardinality 8). Let our possible binary operators be bit-wise and, bit-wise or, bit-wise xor, bit-wise nor, bit-wise xnor, and bit-wise nand. Clearly this is closed because the output is a 3 bit binary number. For each binary operator, determine if the set under that binary operator is a magma, semigroup, or monoid.
**AND:** monoid 
**OR:** monoid
**XOR:** monoid
**NOR:** semigroup
**XNOR:** monoid
**NAND:** semigroup
##### Why can’t strings under concatenation be a group?
Because there is no "inverse string" that you can concatenate to get the identity (in this case an empty string)
##### Polynomials under addition satisfy the property of a group. Demonstrate this is the case by showing it matches all the properties that define a group.
$$\text{Given P is the set of all polynomials with } P_1, P_2, ... P_n \in P$$
$$Closed: P_1 + P_2 = P_3 \in P$$
$$\text{Associative: } P_1 + P_2 = P_2 + P_1$$
$$\text{Identity: } P_1 + 0 = P_1$$
$$\text{Inverse: } P_1 + (-P_1) = 0$$
