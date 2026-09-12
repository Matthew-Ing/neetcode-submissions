class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1

        print (top,bottom, left, right)

        while top<=bottom:
            mid = (top+bottom)//2
            if matrix[mid][0] > target and matrix[mid][right] > target:
                bottom = mid-1
                print("a", top, bottom)
            elif matrix[mid][0] < target and matrix[mid][right] < target:
                top = mid +1
                print("b", top, bottom)
            elif matrix[mid][0] <= target and target <= matrix[mid][right]:
                print("c", top, bottom)
                while left<=right:
                    midc = (left+right)//2
                    print(midc)
                    if target == matrix[mid][midc]:
                        return True
                    elif target > matrix[mid][midc]:
                        left = midc+1
                    elif target < matrix[mid][midc]:
                        right = midc-1
                    else:
                        print("e")
                        return False
                    
            else:
                
                print("d", mid)
                return False
        return False



