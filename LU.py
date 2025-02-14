import numpy as np
import numpy.linalg as la
import random
import scipy

def LU_Decomp(A):
  # print(A)
  m,n = A.shape
  if m > 1:
    alpha = A[0,0]
    v = A[1:,0]
    uT = A[0,1:]
    Astar = A[1:,1:].copy()
    #follow the equations (ignore redundancies)
    beta = alpha #alpha = beta
    xT = uT #uT = xT
    if(beta == 0): print('WARNING! Dividing by 0. Resulting LU may be impacted.')
    w = v/beta #v = beta*w
    #calculate A* = wxT + L*U*
    #Call LU Decomp recursively to retrieve L* and U *
    # result = LU_Decomp(Astar-np.dot(w,xT))
    # apparently, the wx^t is supposed to be a matrix, not a dot product
    # changing from np.dot() to np.outer seems to have corrected the output
    Lstar, Ustar = LU_Decomp(Astar-np.outer(w,xT))
    #create updated L and U
    L = np.eye(m)
    U = np.zeros((m, n))
    # L[0,0] = 1 already done with identity matrix
    L[1:,0] = w
    L[1:,1:] = Lstar
    U[0,0] = beta
    U[0,1:] = xT
    U[1:,1:] = Ustar
    return L, U
  else:
    return np.array([[1]]), A

def checkLU(A, L, U, margin_of_error=0.1):
  print('\n\n****Checking the LU Decomposition****\n')
  print('Margin of error is ' + str(margin_of_error))
  # L2, U2 = scipy.linalg.LU(A)
  _, L2, U2 = scipy.linalg.lu(A)
  Aprime = np.dot(L,U)
  print('scipy reference L and U')
  print('L:\n', L2.round(2))
  print('U:\n', U2.round(2))
  diff = A - Aprime
  diff = np.abs(diff)
  print('Recreated A using LxU: \n' + str(Aprime.round(2)))
  print('Recreation Difference: \n' + str(diff.round(2)))
  errors = np.where(np.abs(diff) > margin_of_error, 1, 0)
  print('\n****Summary****')
  print('Number of Errors with LxU: ' + str(np.sum(errors).round(2)) + '\t Margin of error: ' + str(margin_of_error))
  print('L:\n', L.round(2))
  print('U:\n', U.round(2))
#   print('numpy version:\n' + str(np.linalg.qr(A)[0].round(2)))
#   print(str(np.linalg.qr(A)[1].round(2)))

for i in range(5):  # Run 5 random test cases
    rows = np.random.randint(2, 7)  # Random rows (2 to 6)
    matrix = np.random.randint(1, 100, size=(rows, rows))  # Random values from 1 to 99
    print('\n--------------------------------------------------------------')
    print('---------------------------------------------------------------')
    print('Test Case #' + str(i))
    print('Input Matrix:\n', matrix)

    L, U = LU_Decomp(matrix)  # Assuming your QR function is defined
    # print('Calculated Q:\n', Q.round(2))
    # print('Calculated R:\n', R.round(2))

    checkLU(matrix, L, U)