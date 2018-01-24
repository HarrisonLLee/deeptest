# -*- coding:utf-8 -*-

__author__ = 'VV'

# binary search
# seq: list
# query: target
def binary_search(seq, query):
    # start is start of index
    # end is end of index
    start, end = 0, len(seq) - 1

    while start <= end:
        mid = start + (end - start) // 2  # //aliquot
        val = seq[mid]
        if val == query:
            # find target!
            # return index value
            return mid
        elif val < query:
            # target greater than mid
            # it is between mid and end
            start = mid + 1
        else:
            # target less than mid
            # it is between start and mid
            end = mid - 1

    # target is not belong to seq, return None
    return None


if __name__ == '__main__':
    
    print("Binary search demo")

    print("It is only applicable for an orderly sequence")

    seq = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15]
        
    print(seq)
    print("-------Binary Search-------")
    print("Found: ", 5, " index is: ", binary_search(seq, 5))

    print("-------Binary Search-------")
    print("Found: ", 4, " index is: ", binary_search(seq, 4))

    print("-------Binary Search-------")
    print("Found: ", 13, " index is: ", binary_search(seq, 13))

    print("-------Binary Search-------")
    print("Found: ", 1, " index is: ", binary_search(seq, 1))

    print("-------Binary Search-------")
    print("Found: ", 25, " index is: ", binary_search(seq, 25))