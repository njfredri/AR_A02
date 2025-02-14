
*python dependencies*
numpy  
scipy  
  
You can use 'pip install "package_name"' to install the dependencies.


*How to Run*   
To check QR decomposition on windows, use either './run_Q4_1.bat' or 'python QR.py'  
To check LU decomposition on windows, use either './run_Q4_2.bat' or 'python LU.py'   
  
Both QR and LU decomposition scripts will automatically generate matrix test cases and output their results.  
Results for QR and LU also include checks for correct values. QR has an orthogonal check for Q.   
Q should be either fully orthogonal, semi-orthogonal (for some non-square matrices). It will also say if Q is not orthogonal.

To run Question 5 results on windows, use either './run_Q5.bat' or 'python python Q5c.py'  
Results for question 5 are also included in this document.
Some of the questions in 5 are answered in the pdf rather than this readme.

-----------------------------------------
The images have the following recorded point coordinates:


Image 1
* 1 (331,345)
* 2 (305,357)
* 3 (486,412)
* 4 (477,437)
* 5 (409,451)
* 6 (356,565)
* 7 (251,438)
* 8 (220,466)


Image 2
* 1 (262,471)
* 2 (260,495)
* 3 (421,412)
* 4 (443,426)
* 5 (431,472)
* 6 (531,549)
* 7 (337,569)
* 8 (355,606)


Image 3
* 1 (322,463)
* 2 (317,476)
* 3 (424,458)
* 4 (431,471)
* 5 (411,499)
* 6 (438,563)
* 7 (336,536)
* 8 (337,559)



------------Results-------------

Calculating new H for image 1 -> image 2
H predicted:
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
Total error between projection img1 -> img2 and actual img2: 39.14802447725316

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
Total error between projection img1 -> img3 and actual img3: 292.14802447725316
----------------------------------------------


Calculating new H for image 1 -> image 3
H predicted:
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
Total error between projection img1 -> img2 and actual img2: 257.6123344022093

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
Total error between projection img1 -> img3 and actual img3: 60.161272027928476
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
Total error between projection img2 -> img3 and actual img3: 800.8241991925338

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
Total error between projection img2 -> img3 and actual img3: 358.7078230280603