answer = raw_input("Are You Creating An Entry [Press 1] \nOr Are You Searching An Entry [Press 2] ")

#if we are creating 

if answer == "1" : 
    #print ("This is where we create")
    # collect information

    lastname = raw_input("What is the persons last name? ")
    firstname = raw_input("What is the persons first name? ")
    phone = raw_input("What id the persons phone number? ")
    email = raw_input("What is the persons email address? ")
    address = raw_input("What is the persons address? ")
    date of birth = raw_input("What is the persons date of birth? ")

    #create or search addressbookdata

    temp1 = open("addressbookdata","a")
    
    #create string to print to file
    #print temp1
    #print (firstname + " " + lastname + ", " + phone + ", " + email + ", " + address) 

    temp1.write(firstname + " " + lastname + ", " + phone + ", " + email + ", " + address)
    temp1.write("\n")

# Programme searching for the information

elif answer == "2" :
    print ("this is where we search")
    searchcriteria = raw_input("Enter your search Criteria. Name, Phone Number, Address, Email or Postcode, or Town ")
    print searchcriteria
    temp1 = open("addressbookdata","r")
    for line in temp1:
        if searchcriteria in line:
            print line
        else:
            print("can't find it")
       

#user did not pick or enter information

else :
    print ("Incorrect Answer")
    exit()
