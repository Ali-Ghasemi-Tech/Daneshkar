"""
binary search

"""
def find_numebr(target: int , list: list , start:int , end:int ) -> int:
    answer = 0
    if start > end:
        return "the target number does not exist in this list"
    else:
        mid :int = (start + end )// 2 
        if target > list[mid]:
            find_numebr(target , list , mid , end)
        elif target < list[mid]:
            find_numebr(target , list , start , mid-1)
        else:
            answer = mid
    return answer
        
def binary_search(desired_number:int , *list:list ):
    index = find_numebr(desired_number , list , start= 0 , end=len(list)-1)
    return index
 
    


print(binary_search(9 , 1, 2, 3, 7, 9, 11 ,13))