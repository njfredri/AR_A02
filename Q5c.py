import numpy as np
import numpy.linalg as la
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
    #concatenate Ai into larger 2n * 9 matrix
    A_tot[2*i:2*i+2, :] = Ai
  return A_tot

def compute_H(points1, points2):
  A = compute_nAi(points1, points2)
  print(A.shape)
  ATA = np.dot(A.T, A)
  print(ATA)
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

def check_H(H, points1, points2):
  m,n = points1.shape
  for i in range(m):
    p1 = np.zeros(3)
    p1[0:2] = points1[i,:]
    p1[2] = 1
    p2_pred = np.dot(H, p1)
    p2_pred = p2_pred/p2_pred[2]
    print('\nActual point:\n' + str(points2[i,:]))
    print('Predicted:\n' + str(p2_pred[:2].round(2)))
    print('Error: ' + str(sum(np.abs(points2[i,:] - p2_pred[:2]))))

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
  print('H predicted:\n' + str(H.round(2)))
  return H

def projH(points, H):
    predictpoints = np.zeros(points.shape)
    for i in range(points.shape[0]):
        q = np.ones(3)
        point = points[i,:]
        if point.shape[0] <=2: #add 1 to the end
            q[:2] = point
        else:
            q[:] = point
        #project using H
        temp = np.dot(H,q)
        temp = temp/temp[2] #make 3rd dim 1
        predictpoints[i,:] = temp[:2]
    return predictpoints


img1 = np.array([[331,345],[305,357],[486,412],[477,437],[409,451],[356,565],[251,438],[220,466]])
img2 = np.array([[262,471],[260,495],[421,412],[443,426],[431,472],[531,549],[337,569],[355,606]])
#• Select 4 of the 8 correspondences between images 1 and 2 and find H (2 points).
H1 = compute_H_UsingSVD(img1[:4], img2[:4]) #find h for first 4 points
# check_H(H1, img1, img2)

print('now projecting')
img2_hproj = projH(img1[4:], H1)
print(img2_hproj)
print(img2[4:,:])
print('Total error between projection and actual: ' + str(sum(sum(np.abs(img2[4:,:] - img2_hproj)))))
#Use H to transform the remaining point observations in image 1, projected into image 2
