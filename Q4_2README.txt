To check LU decomposition on windows, use either './run_Q4_2.bat' or 'python LU.py' in command line
An example output is given in Q4_2_output.txt
----------------------------------------------------------------------------------------------
code explaination
----------------------------------------------------------------------------------------------

The LU_Decomp method takes in a Matrix A and returns L U matrices.
The code first works by calculating the alpha, beta, x^T, A*, and w of the input matrix.
Since A*=wx^T + L*U*, L*U* = A*-wx^T.
So LU_Decomp is called recursively with the calculated L*U* matrix.
This recursion repeats until the input matrix is 1x1. Then it will return the
bottom right corners of L and U (aka, returns 1 and A (which is scalar)).
Going back up recursion, L and U are built using the returned L* and U* matrices along
with the previously calculated variables.

The output is the complete L and U matrices.

Similar to Q4_1, this code has a method for checking LU decomposition.
A is "recreated" by multiplying L and U.
Matrix of errors = A(original) - A(recreated)
It calculates the number of elements whose errors are greater than the margin of error.
L and U are calculated with the scipy library to double check the results.
Finally a summary of the errors and the calculated L and U matrices are printed.

------------------------------------------------------------------------------
Sample output for running the QR code:
------------------------------------------------------------------------------


C:\Users\Njfre\AR_A02>python LU.py 

--------------------------------------------------------------
---------------------------------------------------------------
Test Case #0
Input Matrix:
 [[68 37 66]
 [35 49 96]
 [31  1 44]]


****Checking the LU Decomposition****

Margin of error is 0.1
scipy reference L and U
L:
 [[ 1.    0.    0.  ]
 [ 0.51  1.    0.  ]
 [ 0.46 -0.53  1.  ]]
U:
 [[68.   37.   66.  ]
 [ 0.   29.96 62.03]
 [ 0.    0.   46.77]]
Recreated A using LxU: 
[[68. 37. 66.]
 [35. 49. 96.]
 [31.  1. 44.]]
Recreation Difference: 
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]

****Summary****
Number of Errors with LxU: 0	 Margin of error: 0.1
L:
 [[ 1.    0.    0.  ]
 [ 0.51  1.    0.  ]
 [ 0.46 -0.53  1.  ]]
U:
 [[68.   37.   66.  ]
 [ 0.   29.96 62.03]
 [ 0.    0.   46.77]]

--------------------------------------------------------------
---------------------------------------------------------------
Test Case #1
Input Matrix:
 [[ 7 81 62 67 36 44]
 [42 52 59 33 90 90]
 [32 25 54 34 55 59]
 [ 7  5 98 64 44 87]
 [69 55 83 36 38 15]
 [49 40 73 73 15  4]]


****Checking the LU Decomposition****

Margin of error is 0.1
scipy reference L and U
L:
 [[ 1.    0.    0.    0.    0.    0.  ]
 [ 0.1   1.    0.    0.    0.    0.  ]
 [ 0.1  -0.01  1.    0.    0.    0.  ]
 [ 0.71  0.01  0.15  1.    0.    0.  ]
 [ 0.61  0.25 -0.05 -0.03  1.    0.  ]
 [ 0.46 -0.01  0.18  0.19  0.56  1.  ]]
U:
 [[ 69.    55.    83.    36.    38.    15.  ]
 [  0.    75.42  53.58  63.35  32.14  42.48]
 [  0.     0.    89.99  60.83  40.39  85.8 ]
 [  0.     0.     0.    37.59 -18.4  -19.95]
 [  0.     0.     0.     0.    60.44  74.21]
 [  0.     0.     0.     0.     0.    -0.71]]
Recreated A using LxU: 
[[ 7. 81. 62. 67. 36. 44.]
 [42. 52. 59. 33. 90. 90.]
 [32. 25. 54. 34. 55. 59.]
 [ 7.  5. 98. 64. 44. 87.]
 [69. 55. 83. 36. 38. 15.]
 [49. 40. 73. 73. 15.  4.]]
Recreation Difference: 
[[0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0.]]

****Summary****
Number of Errors with LxU: 0	 Margin of error: 0.1
L:
 [[ 1.    0.    0.    0.    0.    0.  ]
 [ 6.    1.    0.    0.    0.    0.  ]
 [ 4.57  0.8   1.    0.    0.    0.  ]
 [ 1.    0.18  4.64  1.    0.    0.  ]
 [ 9.86  1.71  0.41  0.03  1.    0.  ]
 [ 7.    1.21  0.97 -0.85  0.13  1.  ]]
U:
 [[   7.     81.     62.     67.     36.     44.  ]
 [   0.   -434.   -313.   -369.   -126.   -174.  ]
 [   0.      0.     19.59   21.29   -9.33   -3.71]
 [   0.      0.      0.    -37.05   73.3    90.67]
 [   0.      0.      0.      0.    -99.29 -121.72]
 [   0.      0.      0.      0.      0.      3.43]]

--------------------------------------------------------------
---------------------------------------------------------------
Test Case #2
Input Matrix:
 [[41  6 89]
 [ 6  6 95]
 [63 34 66]]


****Checking the LU Decomposition****

Margin of error is 0.1
scipy reference L and U
L:
 [[ 1.    0.    0.  ]
 [ 0.65  1.    0.  ]
 [ 0.1  -0.17  1.  ]]
U:
 [[ 63.    34.    66.  ]
 [  0.   -16.13  46.05]
 [  0.     0.    96.6 ]]
Recreated A using LxU: 
[[41.  6. 89.]
 [ 6.  6. 95.]
 [63. 34. 66.]]
Recreation Difference: 
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]

****Summary****
Number of Errors with LxU: 0	 Margin of error: 0.1
L:
 [[1.   0.   0.  ]
 [0.15 1.   0.  ]
 [1.54 4.84 1.  ]]
U:
 [[  41.      6.     89.  ]
 [   0.      5.12   81.98]
 [   0.      0.   -467.36]]

--------------------------------------------------------------
---------------------------------------------------------------
Test Case #3
Input Matrix:
 [[73 20 69]
 [61 88 57]
 [55 66 72]]


****Checking the LU Decomposition****

Margin of error is 0.1
scipy reference L and U
L:
 [[1.   0.   0.  ]
 [0.84 1.   0.  ]
 [0.75 0.71 1.  ]]
U:
 [[73.   20.   69.  ]
 [ 0.   71.29 -0.66]
 [ 0.    0.   20.48]]
Recreated A using LxU: 
[[73. 20. 69.]
 [61. 88. 57.]
 [55. 66. 72.]]
Recreation Difference: 
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]

****Summary****
Number of Errors with LxU: 0	 Margin of error: 0.1
L:
 [[1.   0.   0.  ]
 [0.84 1.   0.  ]
 [0.75 0.71 1.  ]]
U:
 [[73.   20.   69.  ]
 [ 0.   71.29 -0.66]
 [ 0.    0.   20.48]]

--------------------------------------------------------------
---------------------------------------------------------------
Test Case #4
Input Matrix:
 [[39 38 28 89  4]
 [67 60 47 89 20]
 [18 88 63 27 68]
 [91 15 56 41 54]
 [ 2 98 13 77 52]]


****Checking the LU Decomposition****

Margin of error is 0.1
scipy reference L and U
L:
 [[ 1.    0.    0.    0.    0.  ]
 [ 0.02  1.    0.    0.    0.  ]
 [ 0.2   0.87  1.    0.    0.  ]
 [ 0.43  0.32  0.    1.    0.  ]
 [ 0.74  0.5  -0.    0.44  1.  ]]
U:
 [[ 91.    15.    56.    41.    54.  ]
 [  0.    97.67  11.77  76.1   50.81]
 [  0.     0.    41.68 -47.36  13.08]
 [  0.     0.     0.    47.05 -35.63]
 [  0.     0.     0.     0.   -29.65]]
Recreated A using LxU: 
[[39. 38. 28. 89.  4.]
 [67. 60. 47. 89. 20.]
 [18. 88. 63. 27. 68.]
 [91. 15. 56. 41. 54.]
 [ 2. 98. 13. 77. 52.]]
Recreation Difference: 
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]

****Summary****
Number of Errors with LxU: 0	 Margin of error: 0.1
L:
 [[  1.     0.     0.     0.     0.  ]
 [  1.72   1.     0.     0.     0.  ]
 [  0.46 -13.34   1.     0.     0.  ]
 [  2.33  13.95   0.17   1.     0.  ]
 [  0.05 -18.18  -0.24  -1.49   1.  ]]
U:
 [[  39.     38.     28.     89.      4.  ]
 [   0.     -5.28   -1.1   -63.9    13.13]
 [   0.      0.     35.37 -866.46  241.28]
 [   0.      0.      0.    872.54 -179.66]
 [   0.      0.      0.      0.     81.28]]
