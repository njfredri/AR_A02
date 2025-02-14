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
  print('H calculated:\n' + str(H.round(2)))
  return H

def check_H(H, points1, points2, using='A^TxA to calculate h'):
  '-----------------------Checking----------------'
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
  print('H (using ' + str(using) + '):\n' + str(H.round(2)))
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
  print('H calculated:\n' + str(H.round(2)))
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

def calDistance(points1, points2):
  rawerror = np.abs(points1 - points2)
  rawerrorsq = (rawerror[:,0]*rawerror[:,0])+(rawerror[:,1]*rawerror[:,1])
  distance = np.sqrt(rawerrorsq)
  return sum(distance)

img1 = np.array([[331,345],[305,357],[486,412],[477,437],[409,451],[356,565],[251,438],[220,466]])
img2 = np.array([[262,471],[260,495],[421,412],[443,426],[431,472],[531,549],[337,569],[355,606]])
img3 = np.array([[322,463],[317,476],[424,458],[431,471],[411,499],[438,563],[336,536],[337,559]])
#• Select 4 of the 8 correspondences between images 1 and 2 and find H (2 points).
print('\n\nCalculating new H for image 1 -> image 2')
H1 = compute_H_UsingSVD(img1[:4], img2[:4]) #find h for first 4 points
# check_H(H1, img1, img2)
#Use H to transform the remaining point observations in image 1, projected into image 2


print('\nnow projecting remaining image 1 points to image 2')
img2_hproj = projH(img1[4:], H1)
distance = calDistance(img2[4:,:], img2_hproj)
print('\nactual image2 points:\n' + str(img2[4:,:]))
print('projected to image2:\n' + str(img2_hproj))
print('Total error between projection img1 -> img2 and actual img2: ' + str(distance))
print('Error is sum(Euclidian Distance between projected and actual points)')

# Use H to transform the remaining point observations in image 1, projected into
# image 3. Are these points corrrectly projected in image 3? Why?
# These points are not correctly translated to 3. The error is significantly higher
# This is because H was made with the correspondences of image 1 to image 2, not image 1 to image 3.
print('\nnow projecting remaining image 1 points to image 3')
img3_hproj = projH(img1[4:], H1)
distance = calDistance(img3[4:,:], img3_hproj)
print('\nactual image3 points:\n' + str(img3[4:,:]))
print('projected to image3:\n' + str(img3_hproj))
print('Total error between projection img1 -> img3 and actual img3: ' + str(distance))
print('Error is sum(Euclidian Distance between projected and actual points)')


#Calculate a new H to find point correspondences between images 1 and 3
print('----------------------------------------------')
print('----------------------------------------------')
print('----------------------------------------------')

print('\n\nCalculating new H for image 1 -> image 3')
H2 = compute_H_UsingSVD(img1[:4], img3[:4])

# Can you use the H functions computed earlier to find correspondences between
# images 2 and 3? Explain why

print('\nnow projecting remaining image 1 points to image 2')
img2_hproj = projH(img1[4:], H2)
distance = calDistance(img2[4:,:], img2_hproj)
print('\nactual image2 points:\n' + str(img2[4:,:]))
print('projected to image2:\n' + str(img2_hproj))
print('Total error between projection img1 -> img2 and actual img2: ' + str(distance))
print('Error is sum(Euclidian Distance between projected and actual points)')

print('\npredicted points using H image 1 points to image 3')
img3_hproj = projH(img1[4:], H2)
distance = calDistance(img3[4:,:], img3_hproj)
print('\nactual image3 points:\n' + str(img3[4:,:]))
print('projected to image3:\n' + str(img3_hproj))
print('Total error between projection img1 -> img3 and actual img3: ' + str(distance))
print('Error is sum(Euclidian Distance between projected and actual points)')


#correspondences from image 2 -> 3
print('----------------------------------------------')
print('----------------------------------------------')
print('----------------------------------------------')

print('\npredicted points using H image 2 points to image 3 using first H (aka H of 1->2)')
img3_hproj = projH(img2[4:], H1)
distance = calDistance(img3[4:,:], img3_hproj)
print('\nactual image3 points:\n' + str(img3[4:,:]))
print('projected to image3:\n' + str(img3_hproj))
print('Total error between projection img2 -> img3 and actual img3: ' + str(distance))
print('Error is sum(Euclidian Distance between projected and actual points)')

print('\npredicted points using H image 2 points to image 3 second H (aka H 1->3)')
img3_hproj = projH(img2[4:], H2)
distance = calDistance(img3[4:,:], img3_hproj)
print('\nactual image3 points:\n' + str(img3[4:,:]))
print('projected to image3:\n' + str(img3_hproj))
print('Total error between projection img2 -> img3 and actual img3: ' + str(distance))
print('Error is sum(Euclidian Distance between projected and actual points)')
