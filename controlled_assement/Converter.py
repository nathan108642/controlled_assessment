allowables = ["pounds", "dollars", "euro", "yen"]
rates = [1,1.68,1.23,171.61]
def getChoice(dir):
    answer = None
    while answer not in range(len(allowables)):
        print('Please type the currency code you wish to convert {0}'.format(dir))
        for index, currency in enumerate(allowables):
            print ('enter {0} for {1}'.format(index, currency))
        answer = input("Please type which currency you wish to convert {0} ".format(dir))
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
