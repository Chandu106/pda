#2a
tuple_input_1 = tuple(input("Enter the tuple elements: ").split()) 
tuple_input_2 = tuple(input("Enter the tuple elements: ").split())
summation = []
for i in range(len(tuple_input_1)):
    summation.append(int(tuple_input_1[i]) + int(tuple_input_2[i]))
summation = tuple(summation)
print("Elementwise sum of the tuples: ", summation)
    
#2b
element_1 = tuple_input_1[0]
element_2 = tuple_input_2[2]
element_3 = tuple_input_1[len(tuple_input_1)-1]
element_4 = tuple_input_2[len(tuple_input_1)-1]
new_tuple = (element_1, element_2, element_3, element_4)
print("Specific elements to a new tuple: ", new_tuple)

#2c
title = str(input("Enter the title of the movie: "))
director = str(input("Enter the director name: "))
release_year = int(input("Enter the release year of the movie: "))
budget = int(input("Enter the budget of the movie in cr: "))
movie_tuple = (title, director, release_year, budget)
print("Movie details: ",movie_tuple)
