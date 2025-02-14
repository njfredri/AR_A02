import numpy as np # type: ignore
import numpy.linalg as la # type: ignore
import random

def compute_Ai(p1,p2):
  dim = p1.shape[0]
  w2=1
  x2=p2[0]
  y2=p2[1]
  q = np.ones(3)
  if dim <=2:
    q[0:2] = p1[0:2]
  else:
    w1 = p1[2]
    w2 = p2[2]
    q = p1

  Ai = np.zeros((2,9))
  #first row
  Ai[0,3:6] = -w2 * q.T
  Ai[0,6:9] = y2 * q.T
  #second row
  Ai[1,0:3] = w2 * q.T
  Ai[1, 6:9] = -x2 * q.T
  # print(Ai)
  return Ai

def compute_nAi(points1, points2):
  if len(points1) != len(points2):
    print('Error! Size of points1 and points2 do not match')
  num_points, dim = points1.shape
  A_tot = np.zeros((2*num_points, 9))
  for i in range(num_points):
    #compute A for points
    Ai = compute_Ai(points1[i,:], points2[i,:])
    print('Ai for points ' + str(points1[i,:]) + ',' + str(points2[i,:]))
    print(str(Ai))
    #concatenate Ai into larger 2n * 9 matrix
    A_tot[2*i:2*i+2, :] = Ai
  return A_tot

def compute_H(points1, points2):
  A = compute_nAi(points1, points2)
  print('Single 2x9 matrix A\n' + str(A))
#   print(A.shape)
  ATA = np.dot(A.T, A)
  print('A^T x A:\n' + str(ATA))
  #Find eigen vector with minimum eigen value
  e_val, e_vec = la.eig(ATA)
  min_index = np.argmin(e_val)
  h = e_vec[:, min_index]
  H = np.zeros((3,3))
  H[0,:] = h[0:3]
  H[1,:] = h[3:6]
  H[2,:] = h[6:9]
  for i in range(3):
    for j in range(3):
      H[i,j] = H[i,j] / H[2,2]
  print('H predicted:\n' + str(H.round(2)))
  return H

def check_H(H, points1, points2, desc='using A^TxA to calculate h'):
  m,n = points1.shape
  error = 0
  for i in range(m):
    p1 = np.zeros(3)
    p1[0:2] = points1[i,:]
    p1[2] = 1
    p2_pred = np.dot(H, p1)
    p2_pred = p2_pred/p2_pred[2]
    print('Actual point: ' + str(points2[i,:]))
    print('Point using H: ' + str(p2_pred[:2].round(2)))
    print('Error: ' + str((np.abs(points2[i,:] - p2_pred[:2]))))
    error += la.norm(sum(np.abs(points2[i,:] - p2_pred[:2])))
  print('---------------Summary---------------')
  print('H (' + str(desc) + '):\n' + str(H.round(2)))
  print('Total Error Using H (using euc distance): ' + str(error))


def compute_H_UsingSVD(points1, points2):
  A = compute_nAi(points1, points2)
  #Find eigen vector with minimum eigen value
  u, s, vh = la.svd(A)
  #smallest eigen vector is last in vh
  h = vh[-1,:]
  H = np.zeros((3,3))
  H[0,:] = h[0:3]
  H[1,:] = h[3:6]
  H[2,:] = h[6:9]
  for i in range(3):
    for j in range(3):
      H[i,j] = H[i,j] / H[2,2]
#   print('H predicted:\n' + str(H.round(2)))
  return H

print('\n---------------------------------------\nUsing SVD')
print('--------------------------------------\n')

points1 = np.array([[0,0], [0,1], [1,1], [1,0]])
points2 = np.array([[1,1], [1,0], [2,0], [2,1]])
H = compute_H_UsingSVD(points1, points2)
check_H(H, points1, points2, desc='using SVD to calculate h')