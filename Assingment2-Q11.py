no_of_books = int(input("How many books have you bought this month: "))
if no_of_books < 2 :
    print("You've 0 points.")
elif 2 <= no_of_books < 4 :
    print("You've 5 points.")
elif 4 <= no_of_books < 6 :
    print("You've 15 points.")
elif 6 <= no_of_books < 8 :
    print("You've 30 points.")
elif no_of_books >= 8:
    print("you've 60 points.")
else:
    print("Invalid Input.")
