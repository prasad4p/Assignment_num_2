# Assignment_number_1 
# Question_num_1 = Write a Python program to get a list,sorted in increasing order by the last element in each tuple from a given list of non-empty tuples


tuple = [(2,5), (1,2), (4,4), (2,3), (2,1)] 

print ("Initial list of tuple : ", tuple) 

len = len(tuple) 
for i in range (0, len):   
    for j in range (0, len-i-1):   
        if (tuple [j] [-1] > tuple [j + 1] [-1]):   
            new_value = tuple [j]   
            tuple [j] = tuple [j + 1]   
            tuple [j + 1] = new_value   

print( "Sorted list of tuple in increasing order : " , tuple)  