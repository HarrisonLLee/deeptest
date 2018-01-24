# -*- coding:utf-8 -*-

__author__ = 'VV'

# first binary search
# seq: list
# query: target
def first_binary_search(seq, query):
    # start is start of index
    # end is end of index
    start, end = 0, len(seq) - 1

    while start <= end:
        mid = start + (end - start) // 2  # //aliquot
        val = seq[mid]
        if (mid == 0 and seq[mid] == query) or (seq[mid] == query and seq[mid-1] < query):

            # this is the key for first search
            # find the the target first place
            # return index value
            return mid
        elif seq[mid] < query:
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
    
    print("First Binary search demo")

    print("It is only applicable for an orderly sequence")

    seq = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15]

    # return 7
    print("5 first index value is: ", first_binary_search(seq, 5))

    # return 13
    print("7 first index value is: ", first_binary_search(seq, 7))

    # return 15
    print("8 first index value is: ", first_binary_search(seq, 8))