# https://leetcode.com/problems/image-smoother/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans, temp, row_subresults, len_img, len_img_row, offset = [], [], [], len(img), len(img[0]), 3

        for index_1 in range(len_img):
            temp_1 = index_1 - 1
            start_index_1 = temp_1 if temp_1 > 0 else 0
            end_index_1 = temp_1 + offset if temp_1 + offset < len_img else len_img
            for index_2 in range(len_img_row):
                temp_2 = index_2 - 1
                start_index_2 = temp_2 if temp_2 > 0 else 0
                end_index_2 = temp_2 + offset if temp_2 + offset < len_img_row else len_img_row
                [temp.append(item_2) for item in img[start_index_1:end_index_1] for item_2 in item[start_index_2:end_index_2]]
                row_subresults.append(sum(temp) // len(temp))
                temp = []
    
            ans.append(row_subresults)
            row_subresults = []

        return ans