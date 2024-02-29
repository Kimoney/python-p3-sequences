#!/usr/bin/env python3

def print_fibonacci(length):
    # print out an empty list if length is 0
    if length == 0:
        print(list())
    elif length == 1:
        print(list([0]))
    elif length == 2:
        print(list([0,1]))
    else:
        mylist = []
        for i in range(length):
          if i == 0:
              mylist.append(0)
          elif i == 1:
              mylist.append(1)
          else:
              next_element = mylist[-1] + mylist[-2]
              mylist.append(next_element)
        print(mylist)

