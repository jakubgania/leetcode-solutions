# https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        image_len = len(image)
        for index_1 in range(image_len):
            image[index_1] = image[index_1][::-1]
            for index_2 in range(image_len):
                if image[index_1][index_2] == 0:
                    image[index_1][index_2] = 1
                else:
                    image[index_1][index_2] = 0

        return image