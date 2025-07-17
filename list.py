empty_list = []
print()

numbers = [1,2,3,4,5]
print(numbers)

triples = [1,2,3] * 3
print(triples)

alist = [100,200,300,400,500]
alist = alist [::-1]
print(alist,"\n")

my_list = [1,2,3]
print(len(my_list))

hi_list = [100,'ham',300,55]
print(hi_list[1])
print(hi_list[3])

ham_list = [10,43,56,43,65,45,454,100,"ham","giga"]

print(ham_list[1:9])

# iterate a list
for item in ham_list:
    print(item)
    
ling_list = ham_list + hi_list
print(ling_list)

ham_list.extend(hi_list)
print(ham_list)
L = [4, 3, 1, 7, 9, 5, 10, 8]
print("Original List :-", L)

# variable to store the sum of
# the list
count = 0

# Finding the sum
for i in L:
    count += i

# divide the total elements by
# number of elements
avg = count/len(L)

print("sum = ", count)
print("average = ", avg)

# Sorting the elements of the list
L.sort()

# printing the first element
print("Smallest element is:", L[0])

# printing the last element
print("Largest element is:", L[-1])