To run Question 5a results on windows, use either './run_Q5b.bat' or 'python python Q5b.py'  
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
Next, A^T x A is computed. The linear algebra package is used to calculate all u,s, and vh 
using the provided SVD method. The last vector in vh is selected to be the h vector.
The h vector is then used to construct the H matrix.

Like the previous codes, check_H is used to check how correct the calculated H is.

------------------------------------------------------------------------------
Sample output for running the code:
------------------------------------------------------------------------------


C:\Users\Njfre\AR_A02>python Q5b.py 

---------------------------------------
Using SVD
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
h=last eigen vector from la.svd()
[-4.47213595e-01 -2.90798585e-16 -4.47213595e-01  7.57385268e-18
  4.47213595e-01 -4.47213595e-01  1.04279844e-16 -3.64193712e-16
 -4.47213595e-01]
H calculated:
[[ 1.  0.  1.]
 [-0. -1.  1.]
 [-0.  0.  1.]]
Actual point: [1 1]
Point using H: [1. 1.]
Error: [3.33066907e-16 2.22044605e-16]
Actual point: [1 0]
Point using H: [ 1. -0.]
Error: [6.66133815e-16 2.22044605e-16]
Actual point: [2 0]
Point using H: [ 2. -0.]
Error: [8.88178420e-16 2.22044605e-16]
Actual point: [2 1]
Point using H: [2. 1.]
Error: [4.4408921e-16 4.4408921e-16]
---------------Summary---------------
H (using SVD to calculate h):
[[ 1.  0.  1.]
 [-0. -1.  1.]
 [-0.  0.  1.]]
Total Error Using H (using euc distance): 3.441691376337985e-15
