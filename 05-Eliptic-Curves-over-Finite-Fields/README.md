# Elipitic Curves over Finite Fields
Solutions for the exercises can be found under [exercise-1.py](./exercise-1.py) and [exercise-2.py](./exercise-2.py)
## Errata
| Line | Correction | Reason |
| ---- | ---- | ---- |
| ```from libnum import has_sqrtmod_prime_power, has_sqrtmod_prime_power``` | ```from libnum import has_sqrtmod_prime_power, sqrtmod_prime_power``` | Importing same function twice and ```libnum.sqrtmod_prime_power(5, 11, 1) ```didn't compile for me (need import) |
| Mathplotlib functions | add plt.show() | Optional |
| ```# we might have two solutionsfor sr in square_roots:``` | ```# we might have two solutions<br><br>for sr in square_roots:``` | For loop is inside comment |
| ```next_x, next_y = 4, 10print(1, 4, 10)``` | ```next_x, next_y = 4, 10<br><br>print(1, 4, 10)``` | Print on same line (doesn't compile) |
| ```for i in range(2, 12):``` | ```for i in range(1, 13):``` | Need range 1, 13 to get the same output as specified in the article |
| ```assert eq(add(multiply(G1, 10), multiply(G, 11)), multiply(G1, 21))``` | ```assert eq(add(multiply(G1, 10), multiply(G1, 11)), multiply(G1, 21))``` | G is not defined, should be G1 |
