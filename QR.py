import numpy as np # type: ignore
import numpy.linalg as la # type: ignore
import random

def QR(A):
  m,n = A.shape
  #ai are the columns
  Q = np.zeros((m,n))
  R = np.zeros((n,n))
  for col in range(n):
    ai = A[:,col]
    #set ui to an initial value of ai
    ui = A[:,col].copy().astype(float) #avoids typing issues later
    print('at col ' + str(col))
    for i in range(col):
      #Loop through all previous q and subtract the projection of ai on each q
      # implements    ui = ai - sum( <ai,qk> qk)
      ui = ui - np.dot(Q[:, i], A[:, col]) * Q[:, i]

    #this loop fills in R with the appropriate dot producs
    for i in range(col):
      R[i, col] = np.dot(Q[:,i], A[:,col])
    #the diagonal is just the magnitude of ui
    R[col,col] = la.norm(ui)

    #Use the final ui value to calculate qi
    if la.norm(ui) > 1e-10: #done to fix accuracy issues from before
      Q[:,col] = ui / la.norm(ui)
    else:
      Q[:,col] = 0
  return Q, R


def checkQR(A, Q, R, margin_of_error=0.1):
  print('\n\n****Checking the QR Decomposition****\n')
  print('Margin of error is ' + str(margin_of_error))
  Aprime = np.dot(Q,R)
  diff = A - Aprime
  diff = np.abs(diff)
#   print('Original: \n' + str(A.round(2)))
  print('Recreated A using QxR: \n' + str(Aprime.round(2)))
  print('Recreation Difference: \n' + str(diff.round(2)))
  errors = np.where(np.abs(diff) > margin_of_error, 1, 0)
 
  print("Q^TxQ (should be Identity):\n", np.dot(Q.T, Q).round(2))
  print('\n****Summary****')
  # print('Q is ' + orth)
  print('Number of Errors with QxR: ' + str(np.sum(errors).round(2)) + '\t Margin of error: ' + str(margin_of_error))
  print('Q:\n', Q.round(2))
  print('R:\n', R.round(2))
#   print('numpy version:\n' + str(np.linalg.qr(A)[0].round(2)))
#   print(str(np.linalg.qr(A)[1].round(2)))



for i in range(5):  # Run 5 random test cases
    rows = np.random.randint(2, 7)  # Random rows (2 to 6)
    cols = np.random.randint(2, 7)  # Random cols (2 to 6)
    matrix = np.random.randint(1, 20, size=(rows, cols))  # Random values from 1 to 99
    print('\n--------------------------------------------------------------')
    print('---------------------------------------------------------------')
    print('Test Case #' + str(i))
    print('Input Matrix:\n', matrix)

    Q, R = QR(matrix)  # Assuming your QR function is defined
    # print('Calculated Q:\n', Q.round(2))
    # print('Calculated R:\n', R.round(2))

    checkQR(matrix, Q, R)