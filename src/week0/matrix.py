def mat
    x = y.array([[1,2,3],[3,4,5],[7,8,9]])
        for line in x:
         print ('  '.join(map(str, line)))