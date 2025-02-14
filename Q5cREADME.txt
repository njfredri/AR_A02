To run Question 5c results on windows, use either './run_Q5c.bat' or 'python python Q5c.py'  

----------------------------------------------------------------------------------------------
code explaination
----------------------------------------------------------------------------------------------

The coordinates for points 1-8 in the three images are hard-coded.
To calculate H, compute_H_UsingSVD() from question 5b was chosen.
H would be calculated using points 1-4. Points 5-8 would be used for testing.
method projH would project the provided coordinates using the provided H matrix.
A method for distance was created to track how far all the projected points were from
the real points.

----------------------------------------------------------------------------------------------
answers to some of the questions in Question 5(c)
----------------------------------------------------------------------------------------------
Are these points correctly projected in image 3 (Using first H)? Why?
These are not correctly projected in image 3, but they appear to be relatively close. 
One reason for this is general noise. Another reason is that H was made using the 
correspondences of image 1 and image 2.

Can you use the H functions computed earlier to find correspondences between images 2 and 3?

You cannot use the H functions computed earlier to find correspondences between images 2 and 3. 
This is because of the errors from using a different source image and using a 
different destination image compound. The errors increased significantly when trying to 
do this with both previously computed H functions.

------------------------------------------------------------------------------
Sample output for running the code:
------------------------------------------------------------------------------


C:\Users\Njfre\AR_A02>python Q5c.py 


Calculating new H for image 1 -> image 2
H calculated:
[[ 3.30000e+00  4.56000e+00 -1.86984e+03]
 [ 3.00000e-02  2.16000e+00  6.70140e+02]
 [ 0.00000e+00  0.00000e+00  1.00000e+00]]

now projecting remaining image 1 points to image 2

actual image2 points:
[[431 472]
 [531 549]
 [337 569]
 [355 606]]
projected to image2:
[[432.6515947  467.49927352]
 [537.74526337 544.35114125]
 [337.79117404 575.49296256]
 [358.54296232 616.77448225]]
Total error between projection img1 -> img2 and actual img2: 30.869328066771168
Error is sum(Euclidian Distance between projected and actual points)

now projecting remaining image 1 points to image 3

actual image3 points:
[[411 499]
 [438 563]
 [336 536]
 [337 559]]
projected to image3:
[[432.6515947  467.49927352]
 [537.74526337 544.35114125]
 [337.79117404 575.49296256]
 [358.54296232 616.77448225]]
Total error between projection img1 -> img3 and actual img3: 240.89164105936143
Error is sum(Euclidian Distance between projected and actual points)
----------------------------------------------
----------------------------------------------
----------------------------------------------


Calculating new H for image 1 -> image 3
H calculated:
[[ 1.7400e+00  3.0300e+00 -7.3338e+02]
 [-1.7000e-01  3.2600e+00  2.0734e+02]
 [ 0.0000e+00  0.0000e+00  1.0000e+00]]

now projecting remaining image 1 points to image 2

actual image2 points:
[[431 472]
 [531 549]
 [337 569]
 [355 606]]
projected to image2:
[[411.41482086 492.27666266]
 [437.52355863 544.48995742]
 [340.60921057 526.24303739]
 [342.63631061 544.96585392]]
Total error between projection img1 -> img2 and actual img2: 226.95883355709577
Error is sum(Euclidian Distance between projected and actual points)

predicted points using H image 1 points to image 3

actual image3 points:
[[411 499]
 [438 563]
 [336 536]
 [337 559]]
projected to image3:
[[411.41482086 492.27666266]
 [437.52355863 544.48995742]
 [340.60921057 526.24303739]
 [342.63631061 544.96585392]]
Total error between projection img1 -> img3 and actual img3: 51.166843086812534
Error is sum(Euclidian Distance between projected and actual points)
----------------------------------------------
----------------------------------------------
----------------------------------------------

predicted points using H image 2 points to image 3 using first H (aka H of 1->2)

actual image3 points:
[[411 499]
 [438 563]
 [336 536]
 [337 559]]
projected to image3:
[[462.94340177 463.28695752]
 [561.35805846 441.16097436]
 [537.00462964 559.12234655]
 [580.0547413  559.78895336]]
Total error between projection img2 -> img3 and actual img3: 681.806064168989
Error is sum(Euclidian Distance between projected and actual points)

predicted points using H image 2 points to image 3 second H (aka H 1->3)

actual image3 points:
[[411 499]
 [438 563]
 [336 536]
 [337 559]]
projected to image3:
[[428.27835772 495.53937266]
 [487.64607536 501.94379427]
 [432.66315465 549.99785863]
 [451.29583397 556.69029037]]
Total error between projection img2 -> img3 and actual img3: 308.3051249116028
Error is sum(Euclidian Distance between projected and actual points)
