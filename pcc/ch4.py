magicians = ['alice', 'David', 'Carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I cant wait to see your next trick {magician.title()}")
    print ("Thank you everyone!")
pizza = ['Carbonara', 'Cappricohsa', 'White']
for pizzas in pizza:
    print(f"{pizzas} Thats my favorite!")

for value in range(1, 6):
    numbers = list(range (0, 6))
    even_numbers = list(range(2, 11, 2))
    print(even_numbers)
    squares = []
    for value in range (1,11):
        squares.append(value**2)
    
    print(squares)



squares = [value**2 for value in range(1,11)]
print(squares)
print("Here are the first 3 pizzas:")
for pizzas in pizza[:1]:
    print(pizzas.title())
    my_foods = ['Pizza', 'Canoli',' Carrot Cake']
    friend_foods = my_foods[:]
    print("My favorite foods are:")
    print(my_foods)

    print("\nMy friends favotire foods are")
    print(friend_foods)
    my_foods.append ("Ice Cream")
    print (my_foods)


    
    dimensions = (100, 50)
    print ("Orginal dimensions:")
for dimension in dimensions:
    print(dimension)

    dimensions = (400, 100)
    print("\nModified dimensions:")
    for dimension in dimensions:
        print (dimension)
    