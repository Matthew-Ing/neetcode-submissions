class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # topR = matrix[0][0]
        # bottomR = matrix[len(matrix)-1][0]
        topR = 0
        bottomR = len(matrix)-1

        left = 0
        right = len(matrix[0])-1

        # print(topR, bottomR)
        
        while topR <= bottomR:
            
            midR = (topR + bottomR) // 2
            print("row", midR, matrix[midR][0])
            if target>matrix[midR][0] and target>matrix[midR][len(matrix[0])-1]:
                topR= midR +1
            
            elif target<matrix[midR][0] and target<matrix[midR][len(matrix[0])-1]:
                bottomR=  midR-1

            else:
                print("start")
                print(midR)
                while left<=right:
                    midC = (left + right) // 2
                    print("col", midC, matrix[midR][midC])
                    if target>matrix[midR][midC]:
                        left = midC +1
                    elif target<matrix[midR][midC]:
                        right = midC -1
                    else:
                        return True
                break
                       
        return False