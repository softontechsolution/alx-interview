#!/usr/bin/python3
""" pascal triangle
"""


def pascal_triangle(n):
    """ returns pascal triangle
    """
    if n <= 0:
        return []

    myTran = []

    for i in range(n):
        # first element
        pass_List = [1]
        if i == 0:
            myTran.append(pass_List)
            continue

        k = i - 1
        for j in range(len(myTran[k])):
            if j + 1 == len(myTran[k]):
                # last element
                pass_List.append(1)
                break
            # Add two previous values to get current next value
            passVal = myTran[k][j] + myTran[k][j + 1]
            pass_List.append(passVal)
        myTran.append(pass_List)

    return myTran
