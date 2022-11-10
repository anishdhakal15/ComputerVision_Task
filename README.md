##  Rectangles to work with
<a href="https://drive.google.com/uc?export=view&id=1EFo_eOCoJjAtSlN4Xpw-hE1lSBz7nmjU"><img src="https://drive.google.com/uc?export=view&id=1EFo_eOCoJjAtSlN4Xpw-hE1lSBz7nmjU" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

## Rectangle Numbering Problem

* At first i converted given image to grey scale 
* Then i have applied threshold on greyscale image
* After then i looked for contours and iterate through them
* Approximated each contours Polygons 
* By taking hight and width of contours, i cropped original images into parts
* Because of my limited knowledge on contour selection i cannot find best method to select only lines inside rectangle, so i used a technique in which i made two contours and subtracted on eachother

Two images with different contour selection method

<a href="https://drive.google.com/uc?export=view&id=1ituuQYa7CDzS8CRgICq_X5iYhnIKmn_k"><img src="https://drive.google.com/uc?export=view&id=1ituuQYa7CDzS8CRgICq_X5iYhnIKmn_k" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

Which produces  this image
<a href="https://drive.google.com/uc?export=view&id=1nUHUGhJ27TZXB071Fe-j29Rr8fkbSWzW"><img src="https://drive.google.com/uc?export=view&id=1nUHUGhJ27TZXB071Fe-j29Rr8fkbSWzW" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

Similarly
<a href="https://drive.google.com/uc?export=view&id=1ZBmbBm8ms0fscO_frBPZwPzmoCuAVM1T"><img src="https://drive.google.com/uc?export=view&id=1ZBmbBm8ms0fscO_frBPZwPzmoCuAVM1T" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>


By subtracting them we get following output

<a href="https://drive.google.com/uc?export=view&id=10K-GVwWX_qrv-Pv9WGfCiTmT9iHw-YBY"><img src="https://drive.google.com/uc?export=view&id=10K-GVwWX_qrv-Pv9WGfCiTmT9iHw-YBY" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>



## Rectangle Alignment
To align rectangle i have followed following steps

* At first step , generated contours of each rectangle
* Then, fetched number of angles in which they are tilted
* Applying opencv 2D rotation method to fix their rotation
* Then placed side by side using cv2.concatenate() method
By using these steps following output is generated
<a href="https://drive.google.com/uc?export=view&id=1qKmBVEqFOLlRV8y07-83yg0ch7vXGgW8"><img src="https://drive.google.com/uc?export=view&id=1qKmBVEqFOLlRV8y07-83yg0ch7vXGgW8" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>
