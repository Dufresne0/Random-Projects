import math

print("""
Welcome to the Pisagor Edge 
      
 Press [1] to calculate the pisagor edge     
 Press [2] to calculate the special tringles


""")
veri = input("Enter the process :")

if veri == "1":
    x = input("shEdge1 :")
    x = float(x)
    y = input("shEdge :")
    y = float(y)
    print("Pisagor edge is :", math.sqrt(x ** 2 + y ** 2))

#elif veri == "2":
    #print("Enter one of the short edge")
    #x = input("shortedge :")
    #x = float(x)
    #print("Other edges might be 4 and pisagor might be 5")
