# Rank 1 Constraint Systems 
## Constructing matrix C
Let’s construct the matrix C. We know it will have three rows and eight columns  

$$
    \begin{bmatrix}  
    a_{1,1} & a_{1,out} & a_{1,x} & a_{1,y} & a_{1,z} & a_{1,u} & a_{1,v_1} & a_{1,v_2}\\
    a_{2,1} & a_{2,out} & a_{2,x} & a_{2,y} & a_{2,z} & a_{2,u} & a_{2,v_1} & a_{2,v_2}\\
    a_{3,1} & a_{3,out} & a_{3,x} & a_{3,y} & a_{3,z} & a_{3,u} & a_{3,v_1} & a_{3,v_2}\\
    \end{bmatrix}
$$

With constraints:  

$$
    v_1 = x \times y
$$

$$
    v_2 = z \times u
$$

$$
    out = v_1 \times v_2
$$

First row: v_1  
Second row: v_2  
Third row: out  

Solution (fill in upper matrix):  

$$
    \begin{bmatrix}  
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 \\
    0 & 1 & 0 & 0 & 0 & 0 & 1 & 0 \\
    \end{bmatrix}
$$
