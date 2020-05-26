mass = int(input("Enter object mass in Kilograms: "))
weight = mass * 9.8
if weight > 500:
    print("The object is too heavy.")
elif weight<100 :
    print ("The Object is too light")
else:
    print ("The object is just right.")
