# ObjectTracking_python_OO_IPASS
This is a School project for the education HBO-ICT at the University of applied sciences of Utrecht

---

### The Project:
The company Cobotify wants to make it possible to do small repeating actions with automated Cobots.
To do this the workable meterials need to be fixed in one place so the Cobot can make the adjustments to the meterials.

### The mission
Make a more reliable and precise way to fixate to be edited materials

---

## The code

### [\_\_init\_\_.py](src/__init__.py)
To run the code, run the [\_\_init\_\_.py](src/__init__.py) file, this contains the Main class.
The Main class contains the declaration of the object such as the camera input and the input images.

---

### Applicaion
#### [App](src/Application/App.py)
This python file contains the application where the image output is shown.

---

### imageProcessing
#### [Image](src/imageProcessing/Image.py)
The image Class creates the object with the paramaters for an image, the resolution and the name is to be declared.
##### [StaticImage](src/imageProcessing/StaticImage.py)
This Class is an extend of the Image Class. This Class is to declare pictures.
##### [LiveImage](src/imageProcessing/LiveImage.py)
This class is an extend of the Image Class. This Class is to declare live image feed.

#### [ImageProcessor](src/imageProcessing/ImageProcessor.py)
This class processes the image. It find the contours of the image and compares/matches it with the contours of a second image. 
In this case it is the image out of a 3D draw program called RoboDK. 
It finds the objects that are the same and then draws the outside shape of these objects. 
It also prints the x and y coordinates of the midpoint.

---

### Resources
All the images needed for the program to work without camera

Always use [topview.jpg](src/Resources/topview.jpg) as cam_image, this a picture taken with the camera on the Cobot
For use without live image always use [cameraSideMount\_v1]('Resources/cameraSideMount v1.png') as robodk_image
For use with live image always use [cameraSideMount\_v2]('Resources/cameraSideMount v2.png')

This is because when the live image is read opcv cant use the full res of the camera and steps down to 2048*1536 and i dont know how to fix this


---
##### sources:
    contours: https://learnopencv.com/contour-detection-using-opencv-python-c/#Steps-for-Finding-and-Drawing-Contours-in-OpenCV
    contours midpoint: https://www.geeksforgeeks.org/find-co-ordinates-of-contours-using-opencv-python/
    shapes in images: https://www.pyimagesearch.com/2014/10/20/finding-shapes-images-using-python-opencv/
    



