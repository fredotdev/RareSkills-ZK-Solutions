# Arithmetic Circuits
#### Proving integer division was done properly
quotient * divisor + remainder == numerator
0 <= remainder < b (Proving a number falls into a certain range)
#### Proving a list was sorted
Attack:
	If there is more than one 1 (or another number) in a row or column, you could prove a sorted array with different elements. This is why we can only have one 1 in a raw and column (the rest are 0's).

Contraint:
	Each row and column sum to one
#### Errata
| Line | Corection |
| ---- | ----------- |
| they would be proving 7 / 2 = 2 and the ==quotient is 3==     | remainder is 3            |