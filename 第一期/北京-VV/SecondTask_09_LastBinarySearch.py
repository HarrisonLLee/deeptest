# -*- coding:utf-8 -*-

__author__ = 'VV'

# last binary search
# seq: list
# query: target
def last_binary_search(seq, query):
    # start is start of index
    # end is end of index
    start, end = 0, len(seq) - 1

    while start <= end:
        mid = start + (end - start) // 2  # //aliquot
        val = seq[mid]
        if (mid == len(seq) - 1 and seq[mid] == query) or (seq[mid] == query and seq[mid+1] > query):

            # this is the key for last search
            # find the the target last place
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
    
    print("Last Binary search demo")

    print("It is only applicable for an orderly sequence")

    seq = [1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 10, 13, 15]

    # return 9
    print("5 last index value is: ", last_binary_search(seq, 5))

    # return 14
    print("7 last index value is: ", last_binary_search(seq, 7))

    # return 15
    print("8 last index value is: ", last_binary_search(seq, 8))

    # return 18
    print("15 last index value is: ", last_binary_search(seq, 15))