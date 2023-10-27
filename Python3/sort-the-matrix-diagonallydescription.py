# https://leetcode.com/problems/sort-the-matrix-diagonally/description/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        x_index, y_index, temp_arr = len(mat), len(mat[0]), []
        ans = [[0 for j in range(y_index)] for i in range(x_index)]

        x_index_counter, y_index_counter = x_index, 0
        
        for index in range(x_index + y_index - 1):
            if x_index_counter > 0:
                x_index_counter -= 1
            elif x_index_counter == 0:
                y_index_counter += 1

            temp_x_counter = x_index_counter
            temp_y_counter = y_index_counter

            tmpx = []
            indexes = []

            while True:
                if temp_x_counter > len(mat) - 1 or temp_y_counter > len(mat[0]) - 1:
                    break

                tmpx.append(mat[temp_x_counter][temp_y_counter])
                indexes.append([temp_x_counter, temp_y_counter])
                
                temp_x_counter += 1
                temp_y_counter += 1

            temp_arr_sorted =  sorted(tmpx)
            rx = []

            for index in range(len(temp_arr_sorted)):
                rx.append([temp_arr_sorted[index]] + indexes[index])
            
            temp_arr.append(rx)

        for index in range(len(temp_arr)):
            for pyt in temp_arr[index]:
                ans[pyt[1]][pyt[2]] = pyt[0]
            
        return(ans)