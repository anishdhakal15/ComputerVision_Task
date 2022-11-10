##  Rectangles to work with

<iframe src="https://drive.google.com/file/d/1EFo_eOCoJjAtSlN4Xpw-hE1lSBz7nmjU/preview" width="500" height="380" allow="autoplay"></iframe>

## Rectangle Numbering Problem

* At first i converted given image to grey scale 
* Then i have applied threshold on greyscale image
* After then i looked for contours and iterate through them
* Approximated each contours Polygons 
* By taking hight and width of contours, i cropped original images into parts
* Because of my limited knowledge on contour selection i cannot find best method to select only lines inside rectangle, so i used a technique in which i made two contours and subtracted on eachother

Two images with different contour selection method
<iframe src="https://drive.google.com/file/d/1ituuQYa7CDzS8CRgICq_X5iYhnIKmn_k/preview" width="500" height="380" allow="autoplay"></iframe>

Which produces  this image
<iframe src="https://drive.google.com/file/d/1nUHUGhJ27TZXB071Fe-j29Rr8fkbSWzW/preview" width="500" height="380" allow="autoplay"></iframe>

Similarly
<iframe src="https://drive.google.com/file/d/1ZBmbBm8ms0fscO_frBPZwPzmoCuAVM1T/preview" width="500" height="380" allow="autoplay"></iframe>

By subtracting them we get following output
<iframe src="https://drive.google.com/file/d/10K-GVwWX_qrv-Pv9WGfCiTmT9iHw-YBY/preview" width="500" height="380" allow="autoplay"></iframe>


## Rectangle Alignment
To align rectangle i have followed following steps

* At first step , generated contours of each rectangle
* Then, fetched number of angles in which they are tilted
* Applying opencv 2D rotation method to fix their rotation
* Then placed side by side using cv2.concatenate() method
By using these steps following output is generated
<iframe src="https://drive.google.com/file/d/1qKmBVEqFOLlRV8y07-83yg0ch7vXGgW8/preview" width="500" height="380" allow="autoplay"></iframe>
