def is_present_in_opposite_halves (element,l1:list,l2:list):
    mid1=len(l1)// 2
    mid2= len(l2)// 2
    first_half_l1_second_half_l2 = element in l1[ :mid1] and element in l2[mid2 :]
    elem_in_second_half_and_first_half = element in l1[ mid1:] and element in l2[:mid2 ]
    return first_half_l1_second_half_l2 or elem_in_second_half_and_first_half 
print(is_present_in_opposite_halves(3,[1,2,3,4],[3,2,4,1]))

print(is_present_in_opposite_halves(5,[1,2,3,4],[3,5,4,1]))



