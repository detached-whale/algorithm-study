'''
https://www.testdome.com/questions/python/sorted-search/40608

Implement function count_numbers that accepts a sorted list of unique integers and, efficiently with respect to time used, counts the number of list elements that are less than the parameter less_than.

For example, count_numbers([1, 3, 5, 7], 4) should return 2 because there are two list elements less than 4.
'''

def count_numbers(sorted_list, less_than):
    low = 0
    high = len(sorted_list)
    mid = int((low+high)/2)

    while low != mid:
        if sorted_list[mid] < less_than:
            low = mid
        else:
            high = mid

        mid = int((low+high)/2)
    
    
    if not sorted_list[low] < less_than:
        return 0
    else:
        return low + 1

sorted_list = [1, 3, 5, 7]
print(count_numbers(sorted_list, 8)) # should print 2
