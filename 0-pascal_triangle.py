#!/usr/bin/python3
"""
pascal traingle
"""
def pascal_triangle(n):

    result = []
    if n <= 0:
        return result
    elif n == 1:
        result.append([1])
        return result
    else:
        result.append([1])
        for i in range(n - 1): #TODO: refactor loop for faster time
            prev = result[-1]
            tmp = []
            index = 0
            for i in range(len(prev) -1):
                tmp.append(prev[index] + prev[index+1])
                index += 1
            tmp.insert(0, 1)
            tmp.append(1)
            result.append(tmp)
        return result
