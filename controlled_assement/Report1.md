#report

##Task 1


In this programme i have made a curency converter thats changes the money you type in to a different currency.the design of my programme was to try and make code that acts like a currency converter but try and make as short as i could to fit the users needs.The code needed to convert money from euro, yen, pounds and dollars.This code works and is easy for the user to navigate around the code. 

###Design


In this programme I have made a curency converter.the user told me that i needed to make a code that contain the following:
The code should be able to have exchange rates changed by the user.The user shouldbe able to enter an amount, select the chosen currency for thisand the  currency into which this should be converted.The figure shown should be displayed to two decimal places, for example to the nearest cent in US Dollars.The program uses a numbers 0 to 3 to decide which currency you want to convert to.

####Pseudo code
```
It will ask the user what they want to convert from.
It asks for the numbers 0 to 3.
If the user inputs 0 its pounds, if the user inputs 1 its euros and so on.
After that it then asks what currency you want to convert to.
Once again it asks the user to input 0 to 3 numbers.
It then takes the numbers hte user iputs and multiplys them together.
It then prints or outputs the answer (curreny).
The answer is the value of the two numbers you just multiplyed.
If you enter that you want to convert from pounds, to pounds it just prints the number you entered.
```




```python

allowables = ["pounds", "dollars", "euro", "yen"]
rates = [1,1.68,1.23,171.61]
def getChoice(dir):
    answer = None
    while answer not in range(len(allowables)):
        print('Please type the currency code you wish to convert {0}'.format(dir))
        for index, currency in enumerate(allowables):
            print ('enter {0} for {1}'.format(index, currency))
        answer = input("Please type what currency you wish to convert {0} ".format(dir))
    return (int(answer))
pounds = 'pounds'
dollars = 'dollars'
yen = 'yen'
euro = 'euro'
print("Welcome to the currency converter")

var1 = getChoice ('from')

var2 = getChoice ('to')

var3 = float(input("Please type the amount of currency you wish to convert "))

###Development 

ammount = var3/rates[var1] *rates[var2]
print(' your converted ammount is {0} {1}'.format(ammount,allowables[var2]))
```
####Evaluation
To evaluate my work i have sucesfully made a code that convertes one currency to another.My code is a very sufficient way of converting the to currencies.



