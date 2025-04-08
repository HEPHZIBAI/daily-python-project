'''
Project Description
    Image processing with OpenCV is the topic of today. 
    For this project, we use Python for edge detection. 
    Edge detection is an image processing technique used to identify boundaries or "edges" within an image. 
    These edges represent points where the intensity of the image changes dramatically, such as transitions from light to 
    dark areas, and often correspond to the outlines of objects or regions of interest. 
    This technique is useful in real-world applications such as x-raying, self-driving cars, robotics, etc.

How the Project Works
    The program reads the following PNG file:
    Then, it uses Gaussian blurring via the OpenCV library to smooth out noise for more accurate results. 
    Then, it applies canny edge detection. 
    Finally, we use the matplotlib library to display the result which should be approximately as follows:

Prerequisites
    Required Libraries: cv2, matplotlib
    Installation: pip install opencv-python matplotlib
    Required Files: Download the required files in the “Before Coding” section.
'''