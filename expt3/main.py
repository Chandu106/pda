#3a
set_input_1 = set(input("Enter the set elements: ").split())
set_input_2 = set(input("Enter the set elements: ").split())
print("Common elements in both the sets: ", set_input_1 & set_input_2)

#3b
print("Items which are not common to set1: ", set_input_1 & set_input_2)

#3c
print("Sets are disjoint or not: ", set_input_1.isdisjoint(set_input_2))

