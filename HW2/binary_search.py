"""
binary search

"""
def find_numebr(target: int , list: list , start:int , end:int ) -> int:
    if start > end:
        return "the target number does not exist in this list"
    else:
        if target == list[start]:
            return start
        elif target == list[end]:
            return end
        mid :int = (start + end )// 2 
        if target > list[mid]:
            return find_numebr(target , list , mid +1 , end)
        elif target < list[mid]:
            return find_numebr(target , list , start , mid-1)
        else:
            return mid
        
def binary_search(desired_number:int , *list:list ):
    index = find_numebr(desired_number , list , start= 0 , end=len(list)-1)
    return index
 
    


print(binary_search(7 , 1, 2, 3, 7, 9, 11 ,13))