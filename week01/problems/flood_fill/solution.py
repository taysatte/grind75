
from typing import List

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