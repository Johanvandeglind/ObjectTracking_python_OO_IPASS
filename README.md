# ObjectTracking_python_OO_IPASS
This is a School project for the education HBO-ICT at the University of applied sciences of Utrecht

---

### The Project:
The company Cobotify wants to make it possible to do small repeating actions with automated Cobots.
To do this the workable meterials need to be fixed in one place so the Cobot can make the adjustments to the meterials.

### The mission
Make a more reliable and precise way to fixate the to be edited materials

---

### The code

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
#####[StaticImage](src/imageProcessing/StaticImage.py)
This Class is an extend of the Image Class. This Class is to declare pictures.
#####[LiveImage](src/imageProcessing/LiveImage.py)
This class is an extend of the Image Class. This Class is to declare live image feed.

#### [ImageProcessor](src/imageProcessing/ImageProcessor.py)
This class processes the image. It find the contours of the image and compares/matches it with the contours of a second image. 
In this case it is the image out of a 3D draw program called RoboDK. 
It finds the objects that are the same and then draws the outside shape of these objects. 
It also prints the x and y coordinates of the midpoint.


---



