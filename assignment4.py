distance = int(input("Enter the Distance Travelled "))
if distance >=0 and distance <= 100:
    print("The cost is 5.00$ and the distance travelled is {}".format(distance))
elif distance > 100 and distance <= 500:
    print("The cost is 8.00$ and the distance travelled is {}".format(distance))
elif distance > 500 and distance <= 1000:
    print("The cost is 10.00$ and the distance travelled is {}".format(distance))
elif distance > 1000:
    print("The cost is 12.00$ and the distance travelled is {}".format(distance))
else:
    print("Invalid Distance  Choice")

    # Formatted Outputs

bill = float(input("Enter the  bill paid "))
if  bill >= 0 and  bill <= 50:
     print(" The cost is 0.50 units")
elif bill > 50 and  bill <= 100:
     print("The cost is 1.00 units")
elif bill > 100 and  bill <= 200:
         print("The cost is 1.20 units")
elif bill > 250:
     print("The cost is 1.50 units")
else:
    print("invalid units")


















