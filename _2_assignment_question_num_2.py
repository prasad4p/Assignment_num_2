# Assignment_number_2
# Question_num_2 = Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values



dict = {}
 
for i in range (97, 123):
    dict[chr(i)] = i

print ("Ascii value for alphabet a to z")

print (dict)