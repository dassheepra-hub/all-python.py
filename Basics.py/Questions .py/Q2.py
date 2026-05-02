import csv
def file_to_list(fname):
    result = []
    f = open(fname,"r")
    c = f.readline()
    li = c.strip().split(",")
    for line in f :
        D = dict()
        detail = line.strip().split(",")
        D[li[0]]=detail[0]
        for i in range (1,len(li)): 
            D[li[i]] = int(detail[i])
        result.appen(0)
        return result
    




