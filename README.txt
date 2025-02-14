
*********************python dependencies***************
numpy  
scipy  
  
You can use 'pip install "package_name"' to install the dependencies.
'pip install numpy'
'pip install scipy'

#####################*Python Version Warning*#####################
Python version 3.11.5 used.
In another version of python scipy.linalg.lu() was replaced with scipy.linalg.LU().
If an error with this occurs while running run_Q4_2.bat or LU.py, go to line 41 and 42 to switch which method is being called.

*********************How to Run*************************
To check QR decomposition on windows, use either './run_Q4_1.bat' or 'python QR.py'  
To check LU decomposition on windows, use either './run_Q4_2.bat' or 'python LU.py'   
  
Both QR and LU decomposition scripts will automatically generate matrix test cases and output their results.  
Results for QR and LU also include checks for correct values. QR has an orthogonal check for Q.   
Q should be either fully orthogonal, semi-orthogonal (for some non-square matrices). It will also say if Q is not orthogonal.

To run Question 5a results on windows, use either './run_Q5a.bat' or 'python python Q5a.py'  
To run Question 5a results on windows, use either './run_Q5b.bat' or 'python python Q5b.py'  
To run Question 5c results on windows, use either './run_Q5c.bat' or 'python python Q5c.py'  

Results for question 5 are also included in this document and a separate text files.
Some of the questions in 5 are answered in the pdf rather than this readme.

####################################################################