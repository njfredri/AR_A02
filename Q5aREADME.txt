To run Question 5a results on windows, use either './run_Q5a.bat' or 'python python Q5a.py'  
----------------------------------------------------------------------------------------------
code explaination
----------------------------------------------------------------------------------------------
Compute_H is the highest level method that takes in two sets of points. It then constructs 
matrix A by calling compute_nAi. compute_nAi calls comput_Ai.

The method compute_Ai computes a single 2x9 matrix using two corresponding points. It assumes
W=1 if not provided.
compute_nAi takes in multiple points, computes their Ai, and concatenates all the smaller 2x9
matrices together into one 2nx9 matrix.
This larger A matrix is returned to the compute_H method.
Next, A^T x A is computed. The linear algebra package is used to calculate all eigen vectors 
with corresponding eigen values. The vector with the smallest value is selected to be h.
The h vector is then used to construct the H matrix.

Like the previous codes, check_H is used to check how correct the calculated H is.

------------------------------------------------------------------------------
Sample output for running the code:
------------------------------------------------------------------------------


C:\Users\Njfre\AR_A02>python Q5a.py 

--------------------------------------
Using A^t x A to find h
--------------------------------------

Ai for points [0 0],[1 1]
[[ 0.  0.  0. -0. -0. -1.  0.  0.  1.]
 [ 0.  0.  1.  0.  0.  0. -0. -0. -1.]]
Ai for points [0 1],[1 0]
[[ 0.  0.  0. -0. -1. -1.  0.  0.  0.]
 [ 0.  1.  1.  0.  0.  0. -0. -1. -1.]]
Ai for points [1 1],[2 0]
[[ 0.  0.  0. -1. -1. -1.  0.  0.  0.]
 [ 1.  1.  1.  0.  0.  0. -2. -2. -2.]]
Ai for points [1 0],[2 1]
[[ 0.  0.  0. -1. -0. -1.  1.  0.  1.]
 [ 1.  0.  1.  0.  0.  0. -2. -0. -2.]]
Single 2nx9 matrix A
[[ 0.  0.  0. -0. -0. -1.  0.  0.  1.]
 [ 0.  0.  1.  0.  0.  0. -0. -0. -1.]
 [ 0.  0.  0. -0. -1. -1.  0.  0.  0.]
 [ 0.  1.  1.  0.  0.  0. -0. -1. -1.]
 [ 0.  0.  0. -1. -1. -1.  0.  0.  0.]
 [ 1.  1.  1.  0.  0.  0. -2. -2. -2.]
 [ 0.  0.  0. -1. -0. -1.  1.  0.  1.]
 [ 1.  0.  1.  0.  0.  0. -2. -0. -2.]]
A^T x A:
[[ 2.  1.  2.  0.  0.  0. -4. -2. -4.]
 [ 1.  2.  2.  0.  0.  0. -2. -3. -3.]
 [ 2.  2.  4.  0.  0.  0. -4. -3. -6.]
 [ 0.  0.  0.  2.  1.  2. -1.  0. -1.]
 [ 0.  0.  0.  1.  2.  2.  0.  0.  0.]
 [ 0.  0.  0.  2.  2.  4. -1.  0. -2.]
 [-4. -2. -4. -1.  0. -1.  9.  4.  9.]
 [-2. -3. -3.  0.  0.  0.  4.  5.  5.]
 [-4. -3. -6. -1.  0. -2.  9.  5. 12.]]
H calculated:
[[ 1.  0.  1.]
 [-0. -1.  1.]
 [-0.  0.  1.]]
Actual point: [1 1]
Point using H: [1. 1.]
Error: [6.66133815e-16 4.66293670e-15]
Actual point: [1 0]
Point using H: [1. 0.]
Error: [1.33226763e-15 5.21804822e-15]
Actual point: [2 0]
Point using H: [ 2. -0.]
Error: [6.66133815e-16 3.77475828e-15]
Actual point: [2 1]
Point using H: [2. 1.]
Error: [6.66133815e-16 4.21884749e-15]
---------------Summary---------------
H (using A^TxA to calculate h):
[[ 1.  0.  1.]
 [-0. -1.  1.]
 [-0.  0.  1.]]
Total Error Using H (using euc distance): 2.1205259770340553e-14
