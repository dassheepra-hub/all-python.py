# Write a function named pair_sum that accepts this list 
# as argument it should return the number of pairs of elements in the list thst have a positive sum. if there are no such pairs, return 0. 

def pair_sum (list):
    count =0
    for i in range (len(list)):
        for j in range (i+1,len(list)):
            if list[i] + list[j]>0:
                count+= 1
    return count

example_list = [-2,1,5]
result = pair_sum(example_list)
print(result)
    
