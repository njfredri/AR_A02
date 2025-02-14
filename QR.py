import numpy as np # type: ignore
import numpy.linalg as la # type: ignore
import random

def proj(u,v):
  vu = np.dot(v,u)
  uu = np.dot(u,u)
  return (u*uu)/vu

def QR(A):
  m,n = A.shape
  #ai are the columns
  Q = np.zeros((m,n))
  R = np.zeros((n,n))
  for col in range(n):
    ai = A[:,col]
    ui = A[:,col].copy().astype(float) #avoids typing issues later
    for i in range(col):
      # ui = ui - (proj(Q[:,i],A[:,col]))
      #use dot product instead according to summation form
      #        sum ( <ai,qk> qk)
      ui = ui - np.dot(Q[:, i], A[:, col]) * Q[:, i]

    for i in range(col):
      R[i, col] = np.dot(Q[:,i], A[:,col])

    R[col,col] = la.norm(ui)
    if la.norm(ui) > 1e-10: #done to fix accuracy issues from before
      Q[:,col] = ui / la.norm(ui)
    else:
      Q[:,col] = 0
  return Q, R


def checkReduction(A, Q, R, margin_of_error=0.1):
  print('\n\n****Checking the QR Decomposition****\n')
  print('Margin of error is ' + str(margin_of_error))
  Aprime = np.dot(Q,R)
  diff = A - Aprime
  diff = np.abs(diff)
#   print('Original: \n' + str(A.round(2)))
  print('Recreated A using QxR: \n' + str(Aprime.round(2)))
  print('Recreation Difference: \n' + str(diff.round(2)))
  errors = np.where(np.abs(diff) > margin_of_error, 1, 0)
  qqt = np.dot(Q.T, Q)
  is_orth1 = True
  for i in range(qqt.shape[0]):
    for j in range(qqt.shape[1]):
        if i==j: #should be 1
          if qqt[i,j] > (1.0+0.1*margin_of_error): 
             is_orth1=False
          if qqt[i,j] < (1.0-0.1*margin_of_error):
             is_orth1=False
        #   print(qqt[i,j])
        else: #should be 0
            if qqt[i,j] > (0.0+0.1*margin_of_error): is_orth1=False
            if qqt[i,j] < (0.0-0.1*margin_of_error): is_orth1=False
  is_orth2 = True
  qqt = np.dot(Q, Q.T)
  for i in range(qqt.shape[0]):
    for j in range(qqt.shape[1]):
        if i==j: #should be 1
          if qqt[i,j] > (1.0+0.1*margin_of_error): 
             is_orth2=False
          if qqt[i,j] < (1.0-0.1*margin_of_error):
             is_orth2=False
        #   print(qqt[i,j])
        else: #should be 0
            if qqt[i,j] > (0.0+0.1*margin_of_error): is_orth2=False
            if qqt[i,j] < (0.0-0.1*margin_of_error): is_orth2=False
  square = True
  if Q.shape[0] != Q.shape[1]: square=False
  orth = 'Fully Orthogonal'
  if square==False: #non-square matrix can be semi orthogonal
    if is_orth1 == False and is_orth2 == True:
        orth = 'Semi Orthogonal'
    elif is_orth1 == True and is_orth2 == False:
        orth = 'Semi Orthogonal'
  if is_orth1 == False and is_orth2 == False:
     orth = 'Not Orthogonal'
  print("QxQ^T (should be Identity):\n", np.dot(Q, Q.T).round(2))
  print("Q^TxQ (should be Identity):\n", np.dot(Q.T, Q).round(2))
  print('\n****Summary****')
  print('Q is ' + orth)
  print('Number of Errors with QxR: ' + str(np.sum(errors).round(2)) + '\t Margin of error: ' + str(margin_of_error))
  print('Q:\n', Q.round(2))
  print('R:\n', R.round(2))
#   print('numpy version:\n' + str(np.linalg.qr(A)[0].round(2)))
#   print(str(np.linalg.qr(A)[1].round(2)))



for i in range(5):  # Run 5 random test cases
    rows = np.random.randint(2, 7)  # Random rows (2 to 6)
    cols = np.random.randint(2, 7)  # Random cols (2 to 6)
    matrix = np.random.randint(1, 100, size=(rows, cols))  # Random values from 1 to 99
    print('\n--------------------------------------------------------------')
    print('---------------------------------------------------------------')
    print('Test Case #' + str(i))
    print('Input Matrix:\n', matrix)

    Q, R = QR(matrix)  # Assuming your QR function is defined
    # print('Calculated Q:\n', Q.round(2))
    # print('Calculated R:\n', R.round(2))

    checkReduction(matrix, Q, R)