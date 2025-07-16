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