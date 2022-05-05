# Automatic Calculus Software

An application that uses openCV and Images Processing. 

Its main role is when entering an image containing a mathematical operation to calculate, the end result is showing the final number of that equation.

First, it starts by recognizing the operation drawn in the images, convert it into a string and calculates it.


![Figure_1](https://user-images.githubusercontent.com/62222721/166967495-80bd4c9f-de73-4e22-983d-d803afbc5d1b.png)
![Figure_2](https://user-images.githubusercontent.com/62222721/166967502-edcc75b3-66f5-4c94-a7a1-b592f5797ae0.png)
![Figure_3](https://user-images.githubusercontent.com/62222721/166967503-d3d1cc67-85d0-4ecc-80cd-91d64342b20f.png)
![Figure_4](https://user-images.githubusercontent.com/62222721/166967505-e670af19-f570-4341-aea8-651c441c824d.png)


# ** Unit Testing **
4 aspects where tested
-  the function that transforms the image into a string : **test_img2string**
-  the function that transforms the string into a result : **test_string2op**
-  the function that transforms the string into a result (if we provide a division by 0) : **test_string2op**
-  the function that transforms the image into a result number : **test_calculus**

# Output:

![output](https://user-images.githubusercontent.com/62222721/166967461-36e7941e-5280-4ad4-9e0b-c9223f529ea9.png)

