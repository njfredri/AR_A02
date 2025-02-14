To check QR decomposition on windows, use either './run_Q4_1.bat' or 'python QR.py' in command line
An example output is given in Q4_1_output.txt

----------------------------------------------------------------------------------------------
code explaination
----------------------------------------------------------------------------------------------
The QR method takes in matrix A and returns the Q and R matrices.
First, it creates arrays of 0 for Q and R.
Then, the program goes column by column.
For each column, i, ui is initially set to ai. After that, the code will
loop through all previous q. The projection of ai on each q is subtracted from
ui.
After that loop, ui's value is finalized.
Next, another loop will fill in the non-diagonal of a column in R.

The diagonal element in the current column of R is set to the norm of ui.
At the end of the loop, the latest qi is calculated and added to the Q matrix.

After looping through all columns, the Q and R matrices are returned.


The python program will automatically generate and test 5 matrices of random size and value.
Another method was added to check the QR decomposition.
The first thing that is checked is if QxR = A. Then the difference/error in the calculation is printed.
To account for innaccuracies with floating-point variables, a margin of error is used.
The number of elements exceeding the margin in the error matrix are counted.
The product of Q^T x Q is given to show if qi form an orthonormal basis.

Finally, a summary is given printing the error count along with the calculated Q and R.






------------------------------------------------------------------------------
Sample output for running the code:
------------------------------------------------------------------------------

C:\Users\Njfre\AR_A02>python QR.py 

--------------------------------------------------------------
---------------------------------------------------------------
Test Case #0
Input Matrix:
 [[ 4 11 16 14]
 [17 11 10  5]
 [ 9 15 13 17]
 [13 16 17 14]]
at col 0
at col 1
at col 2
at col 3


****Checking the QR Decomposition****

Margin of error is 0.1
Recreated A using QxR: 
[[ 4. 11. 16. 14.]
 [17. 11. 10.  5.]
 [ 9. 15. 13. 17.]
 [13. 16. 17. 14.]]
Recreation Difference: 
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
Q^TxQ (should be Identity):
 [[ 1.  0. -0. -0.]
 [ 0.  1. -0.  0.]
 [-0. -0.  1.  0.]
 [-0.  0.  0.  1.]]

****Summary****
Number of Errors with QxR: 0	 Margin of error: 0.1
Q:
 [[ 0.17  0.6   0.69  0.36]
 [ 0.72 -0.58  0.14  0.35]
 [ 0.38  0.5  -0.7   0.33]
 [ 0.55  0.22  0.09 -0.8 ]]
R:
 [[23.56 24.36 24.28 20.21]
 [ 0.   11.37 14.19 17.21]
 [ 0.    0.    4.8  -0.38]
 [ 0.    0.    0.    1.23]]

--------------------------------------------------------------
---------------------------------------------------------------
Test Case #1
Input Matrix:
 [[17 18  9  3  5  8]
 [18  3 19 16 11  8]
 [16  3  6 19 18  7]
 [10  8 16  9 12 10]
 [18 11  6  2  5  1]
 [13  2  2  7 18  9]]
at col 0
at col 1
at col 2
at col 3
at col 4
at col 5


****Checking the QR Decomposition****

Margin of error is 0.1
Recreated A using QxR: 
[[17. 18.  9.  3.  5.  8.]
 [18.  3. 19. 16. 11.  8.]
 [16.  3.  6. 19. 18.  7.]
 [10.  8. 16.  9. 12. 10.]
 [18. 11.  6.  2.  5.  1.]
 [13.  2.  2.  7. 18.  9.]]
Recreation Difference: 
[[0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]]
Q^TxQ (should be Identity):
 [[ 1. -0. -0. -0.  0.  0.]
 [-0.  1.  0.  0.  0. -0.]
 [-0.  0.  1.  0.  0. -0.]
 [-0.  0.  0.  1.  0. -0.]
 [ 0.  0.  0.  0.  1. -0.]
 [ 0. -0. -0. -0. -0.  1.]]

****Summary****
Number of Errors with QxR: 0	 Margin of error: 0.1
Q:
 [[ 0.44  0.72 -0.1   0.17 -0.11  0.49]
 [ 0.47 -0.42  0.53 -0.29 -0.35  0.32]
 [ 0.42 -0.35 -0.23  0.75 -0.18 -0.21]
 [ 0.26  0.23  0.64  0.17  0.53 -0.39]
 [ 0.47  0.16 -0.32 -0.5  -0.2  -0.6 ]
 [ 0.34 -0.32 -0.37 -0.2   0.71  0.31]]
R:
 [[ 38.24  18.62  23.15  22.49  26.55  16.4 ]
 [  0.    13.57   0.29 -11.18  -9.6   -0.54]
 [  0.     0.    15.43   6.33   0.55   4.58]
 [  0.     0.     0.     9.43   7.33   3.83]
 [  0.     0.     0.     0.    10.59   6.6 ]
 [  0.     0.     0.     0.     0.     3.26]]

--------------------------------------------------------------
---------------------------------------------------------------
Test Case #2
Input Matrix:
 [[15 11]
 [12 19]
 [18  4]
 [ 1 13]]
at col 0
at col 1


****Checking the QR Decomposition****

Margin of error is 0.1
Recreated A using QxR: 
[[15. 11.]
 [12. 19.]
 [18.  4.]
 [ 1. 13.]]
Recreation Difference: 
[[0. 0.]
 [0. 0.]
 [0. 0.]
 [0. 0.]]
Q^TxQ (should be Identity):
 [[1. 0.]
 [0. 1.]]

****Summary****
Number of Errors with QxR: 0	 Margin of error: 0.1
Q:
 [[ 0.57  0.04]
 [ 0.46  0.58]
 [ 0.68 -0.46]
 [ 0.04  0.67]]
R:
 [[26.34 18.14]
 [ 0.   18.38]]

--------------------------------------------------------------
---------------------------------------------------------------
Test Case #3
Input Matrix:
 [[16  3  7  6]
 [15 19 18  2]
 [ 3  9  5 11]]
at col 0
at col 1
at col 2
at col 3


****Checking the QR Decomposition****

Margin of error is 0.1
Recreated A using QxR: 
[[16.  3.  7.  6.]
 [15. 19. 18.  2.]
 [ 3.  9.  5. 11.]]
Recreation Difference: 
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
Q^TxQ (should be Identity):
 [[ 1. -0. -0.  0.]
 [-0.  1. -0.  0.]
 [-0. -0.  1.  0.]
 [ 0.  0.  0.  0.]]

****Summary****
Number of Errors with QxR: 0	 Margin of error: 0.1
Q:
 [[ 0.72 -0.64 -0.26  0.  ]
 [ 0.68  0.58  0.45  0.  ]
 [ 0.14  0.5  -0.86  0.  ]]
R:
 [[ 22.14  16.26  17.93   7.18]
 [  0.    13.66   8.52   2.8 ]
 [  0.     0.     1.95 -10.08]
 [  0.     0.     0.     0.  ]]

--------------------------------------------------------------
---------------------------------------------------------------
Test Case #4
Input Matrix:
 [[11 13  9]
 [19  1 18]
 [ 2 12  7]]
at col 0
at col 1
at col 2


****Checking the QR Decomposition****

Margin of error is 0.1
Recreated A using QxR: 
[[11. 13.  9.]
 [19.  1. 18.]
 [ 2. 12.  7.]]
Recreation Difference: 
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
Q^TxQ (should be Identity):
 [[ 1. -0. -0.]
 [-0.  1. -0.]
 [-0. -0.  1.]]

****Summary****
Number of Errors with QxR: 0	 Margin of error: 0.1
Q:
 [[ 0.5   0.56 -0.66]
 [ 0.86 -0.4   0.31]
 [ 0.09  0.72  0.69]]
R:
 [[22.05  8.44 20.64]
 [ 0.   15.58  2.88]
 [ 0.    0.    4.44]]
