'''
1. Write a function that takes in a three-digit integer and returns the “flipped” version 
(that is, with its digits reversed). For example: 
 
  Enter a positive number less than 1000:  177 
  That number flipped is 771 
 
Hint: Represent the users input as a integer and use the arithmetic operators // and % to 
do it. 
'''

def flip(number):
    reverse = str(number)[::-1]
    return reverse

def flipper(number):
    hundredPlace = number//100
    tensPlace = (number%100)//10
    onesPlace = (number%100)%10
    return onesPlace*100 + tensPlace*10 + hundredPlace

print(flip(123))
print(flipper(8))

'''
#2. Write a function that asks a user for a positive integer, and then prints the minimum 
number of quarters, dimes, nickels, and pennies needed to make up that amount.  For 
example: 
 
Enter an amount:  67 
 
2 quarter(s), 1 dime(s), 1 nickel(s), 2 penny(ies) 
'''

def minCoins(number):
    quarter = number//25
    dime = number%25//10
    nickel = number%25%10//5
    pennie = number%25%10%5
    
    print(quarter,"quarters(s),",dime,"dime(s),",nickel,"nickel(s),",pennie,"penny(ies)")
    return

minCoins(67)

'''
#3. Write a program that asks a user for a floating point number and that then prints two 
values:  the number truncated to the first decimal place and the number rounded to the 
first decimal place.  For example: 
 
  Enter a number:  4.158 
  Truncated to one decimal place:  4.1 
  Rounded to one decimal place:  4.2 
 
Hint: Have a look at the math module.  '''


def roundingFloatingPoint():
    number = float(input("Enter a number:  "))
    print("Rounded to one decimal place: ",int((number*10))/10)
    print("Rounded to one decimal place: ",round(number,1))
#roundingFloatingPoint()


'''#4. Write a little trigonometry progam.  Ask a user for an angle, specified in degrees.  
Then print the sine, cosine, and tangent of that angle.   For example: 
 
  Enter an angle:  60. 
  sin(60.00) is 0.866025 
  cos(60.00) is 0.500000 
  tan(60.00) is 1.732051 
 '''
import math
from tarfile import FIFOTYPE
import telnetlib

def angleToRad(angle):
    print("sin(" + str(angle) + ") is " + str(round(math.sin(math.radians(angle)),6)))
    print("cos(" + str(angle) + ") is " + str(round(math.cos(math.radians(angle)),6)))
    print("tan(" + str(angle) + ") is " + str(round(math.tan(math.radians(angle)),6)))

angleToRad(60)

'''#5. Write a program that takes the role of a store clerk.  Ask a user to enter two floating 
point numbers:  the cost of an item and the amount of money remitted to pay for the item.  
Then  respond  appropriately:    calculate  the  change  due  to  the  customer  or  ask  the 
customer for more money.  For example: 
 
Cost of the item:  3.56 
Amount tendered:  5.00 
Change:  1.44 
 
or 
 
Cost of the item:  3.56 
Amount tendered:  3.00 
Still due:  0.56 '''

def cashier():
    cost = float(input("Cost of the item: "))
    amount = float(input("Amount tendered: "))
    print("Change: ",float(amount)-float(cost))
    
#cashier()

'''#6.  Combine  #5  with  #2:  if  in  #5  you  owe  the  customer  some  change,  calculate  the 
minimum number of $100, $50, $20, $10, $5, toonies, loonies, quarters, dimes, nickels, 
and pennies needed to make up that amount. Modify the function from #2 to print out the 
way to make the change. 
'''

def cashier2():
    cost = float(input("Cost of the item: "))
    amount = float(input("Amount tendered: "))
    change = (amount - cost)
    
    hundred = change//100
    fifty = change%100//50
    twenty = change%100%50//20
    ten = change%100%50%20//10
    five = change%100%50%20%10//5
    toonie = change%100%50%20%10%5//2
    loonie = change%100%50%20%10%5%2//1
    quarter = change%100%50%20%10%5%2%1*100//25
    dime = change%100%50%20%10%5%2%1*100%25//10
    nickel = change%100%50%20%10%5%2%1*100%25%10//5
    pennie = change%100%50%20%10%5%2%1*100%25%10%5

    print(hundred,"hundred,",fifty,"fifty,",twenty,"twenty,",ten,"tens,",five,"five,",toonie,"toonie,",loonie,"loonie,",quarter,"quarters(s),",dime,"dime(s),",nickel,"nickel(s),",pennie,"penny(ies)")

#cashier2()

 
'''#7. Your code for #6 doesn’t work in Canada since we no longer have pennies. Fix it to 
work in Canada. (Hint: How do stores make change when the amount isn't a multiple of 
5?) '''
def cashier3():
    cost = float(input("Cost of the item: "))
    amount = float(input("Amount tendered: "))
    change = (amount - cost)
    
    hundred = change//100
    fifty = change%100//50
    twenty = change%100%50//20
    ten = change%100%50%20//10
    five = change%100%50%20%10//5
    toonie = change%100%50%20%10%5//2
    loonie = change%100%50%20%10%5%2//1
    quarter = change%100%50%20%10%5%2%1*100//25
    dime = change%100%50%20%10%5%2%1*100%25//10
    nickel = change%100%50%20%10%5%2%1*100%25%10//5
    pennie = change%100%50%20%10%5%2%1*100%25%10%5

    if pennie >= 3:
        nickel += 1
        
    print(hundred,"hundred,",fifty,"fifty,",twenty,"twenty,",ten,"tens,",five,"five,",toonie,"toonie,",loonie,"loonie,",quarter,"quarters(s),",dime,"dime(s),",nickel,"nickel(s)")

#cashier3()

 
'''#8. Write a function that takes a positive integer input less than 100000 and returns an 
integer  corresponding  to  the  number  of  digits  in  the  number.  Use  this  function  in  a 
program that prompts the user for an integer and prints the number of digits in the user’s 
input. [Note: there are a number of ways to solve this problem. It is pretty easy if you do 
it with a string. You should also try it directly with an integer.] 
'''
def numberOfIntegers(number):
    print(len(str(number)))

numberOfIntegers(95604)

'''#9. Water exists in three states- solid, liquid, and gas. Write a function that takes in the 
temperature in Celsius and returns a string “solid”, “liquid”, or “gas” depending on the 
temperature. Write a program using this function that prompts the user for a temperature 
and prints out the resulting state of water.  
'''




 