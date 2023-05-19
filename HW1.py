# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:03:35 2023

@author: w1594
"""
# Exercise 2
#1. Define a fraction number with numerator=123 and denominator=456, print out the fraction number in format a/b and the quotient with 8 digits after decimal point.
numerator = 123
denominator = 456
print(str(numerator) + '/' + str(denominator) +'=' + str(round(numerator / denominator, 8)))
print(str(numerator) + '/' + str(denominator) +'=' + format(str(numerator / denominator),'.10s'))

# 2.Print out every other character of the string "Data Science" using string slicing.
data = 'Data Science'
print(data[::2])

# 3. The string `regex_wiki` contains the second paragraph of regular expression 
#introduction in Wikipedia. Modify the string with all lower case and no space.
regex_wiki = """The concept arose in the 1950s when the American mathematician Stephen Cole Kleene formalized 
the description of a regular language. The concept came into common use with Unix text-processing utilities. 
Different syntaxes for writing regular expressions have existed since the 1980s, one being the POSIX standard 
and another, widely used, being the Perl syntax."""
regex_wiki.lower().replace(' ','')

 

#4. Replace all data with <3 in the following string. Use a string method to check data is not in the new string.
data_science = """Data science continues to evolve as one of the most promising and in-demand career paths for 
skilled professionals. Today, successful data professionals understand that they must advance past the traditional 
skills of analyzing large amounts of data, data mining, and programming skills. In order to uncover useful 
intelligence for their organizations, data scientists must master the full spectrum of the data science life cycle 
and possess a level of flexibility and understanding to maximize returns at each phase of the process."""
modified = data_science.replace('data', '<3')
print(modified)
print('\n')
print('data' in modified)
data_science.replace('data', '<3')



# Exercise 3
score = 99
if score >= 90:
    grade = 'A'
elif score >= 80 and score < 90:
    grade = 'B'
elif score >= 70 and score < 80:
    grade = 'C'
elif score >= 60 and score < 70:
    grade = 'D'
else:
    grade = 'F'
print(grade)



x=1
y=1
if x < y:
    print('x is less than y')
elif x > y:
    print ('x is greater than y')
else:
    print('x  is the same as y')

# Exercise 4

test_list = [1,2,3,'a','b','c']
print(test_list)
test_list.extend('data')
print(test_list)
test_list.count('a')

# 2. How can you check if a key is already in a dictionary? Give an example.
'key' in one_dict.keys()

fibolist=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811]

fibolist[-1]
sum(fibolist)
fibolist.append(fibolist[-1] + fibolist[-2])
fibolist

fibolist_1 = fibolist.copy()
fibolist_1.reverse()
print(fibolist_1)

fibo_29473 = 29473 in fibolist
fibo_29473

# Create two sets. Calculate the union, intersection, difference and symmetric difference for the two sets.
one_set = set('edward wang')
two_set = {1,9,9,7,'H','a','n','g'}
print(one_set)
print(two_set)
print(one_set | two_set) #union
print(one_set & two_set) #intersection
print(one_set ^ two_set) #difference
print(one_set - two_set) #letters in one_set but not in two_set

# Creat a dictionary using at least two different methods.
dict1 = dict(Edward='Hanqing', Wang=1997)
print(dict1)
dict2 = {'Edward':'Hanqing', 'Wang': 1997}
print(dict2)
1997 in dict1.values()

fibo_dict = {} #创建了一个dictionary
num = 555  
fibo_dict[num] = num in fibolist   #append key and value, syntax: dict[key] = value
fibo_dict


