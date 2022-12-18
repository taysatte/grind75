# Flood Fill

```
Author: Taylor Sattenfield
Date: 17 December 2022
```

## Problem

An image is represented by an ```m x n``` integer grid ```image``` where ```image[i][j]``` represents the pixel value of the image.

You are also given three integers ```sr```, ```sc``` and ```color```. You should perform a <b>flood fill</b> on the image starting from the pixel ```image[sr][sc]```.

To perform a <b>flood fill</b>, consider the starting pixel, plus any pixels connected <b>4-directionally</b> to the starting pixel of the same color as the starting pixel, plus any pixels connected <b>4-directionally</b> to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with ```color```.

Return <i>the modified image after performing the flood fill.</i>

### Example 1:
<br>
<img src="https://i.ibb.co/Lg2Fqns/flood.png" alt="flood" border="0"></a>
<br><br>

```
Input: image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr = 1, sc = 1, color = 2
Output: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color. (Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel)
```
### Example 2:

```
Input: image = [[0, 0, 0], [0, 0, 0]], sr = 0, sc = 0, color = 0
Output: [[0, 0, 0], [0, 0, 0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
```

Constraints:<br>

```m == image.length```<br><br>
```n == image[i].length```<br><br>
```1 <= m, n <= 50```<br><br>
```0 <= image[i][j], color < 2^16```<br><br>
```0 <= sr < m```<br><br>
```0 <= sc < n```<br><br>

# Explanation

This problem is great for building a mental visualization of the depth-first search algorithm. It's basically a "fill" function used in a lot of popular editing applications. Here's how the algorithm works:

<ul>
<li>We need to establish a main function <i>flood_fill()</i> for returning the final image and a recursive helper function <i>fill()</i> to do the recoloring
<li>Our base case in the main function will be to catch if the initial color is the same as the color we want to change it to, if it is we will return the image
<li>If it needs to be changed we call our recursive helper function <i>fill()</i>
<li>We pass in the <i>image</i>, <i>sr</i>, <i>sc</i>, <i>image[sr][sc]</i> (current color of pixel), and <i>new_color</i>
<li>The base case for our recursive function will check if the <i>sr</i> and <i>sc</i> variables are out of bounds during the recursive calls as well as if the pixel's color is not equal to the new color
<li>Once the base case is met for all of the applicable pixels it will return to our main function and return the new <i>image</i>
</ul>


``` python3
class Solution:
    def flood_fill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        self.fill(image, sr, sc, image[sr][sc], color)
        return image

    def fill(self, image: List[List[int]], sr: int, sc: int, color: int, new_color: int):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[sr]) or image[sr][sc] != color:
            return

        image[sr][sc] = new_color
        self.fill(image, sr + 1, sc, color, new_color) # Down 
        self.fill(image, sr - 1, sc, color, new_color) # Up
        self.fill(image, sr, sc + 1, color, new_color) # Right
        self.fill(image, sr, sc - 1, color, new_color) # Left
```