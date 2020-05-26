seconds=int(input("Enter number of seconds: "))
product = 0
difference=0
new_seconds = 0
minutes = int(seconds/60)
hours =int(seconds/3600)
days = int(seconds/86400)

if  seconds < 60 :
    print(str(seconds) + " Seconds")
elif 60<= seconds < 3600:
    product= minutes*60
    difference = seconds - product
    print(str(minutes) + " mins " + str(difference) + " seconds." )
elif (seconds>60) and (seconds >= 3600) and (seconds < 86400):
  product = hours * 3600
  new_seconds = seconds - product
  minutes = int(new_seconds/60)
  product = minutes*60
  difference = new_seconds - product
  print(str(hours)+" hours " + str(minutes) + " minutes " + str(difference) + " seconds.") 
elif  (seconds >= 86400): 
    product = days*86400
    new_seconds = seconds - product
    hours = int(new_seconds/3600)
    product = hours * 3600
    difference = new_seconds - product
    minutes = int(difference/60) 
    product = minutes*60
    new_seconds = difference - product
    print(str(days) + " days " + str(hours)+" hours " + str(minutes) + " minutes " + str(new_seconds) + " seconds.")
