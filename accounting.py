
def incorrect_payment_list(path): #create a function with a file/path as the parameter
    """Prints a list of customers whose payments were incorrect
     and what that payment was compared to the expected amount"""
    payment_list = open(path) #open the file

    for line in payment_list: #for loop iterates over file lines
        line = line.rstrip()
        content = line.split('|') #splits file lines by '|' to make a list of strings

        unknown_number = content[0] #not sure what the first number in the file means. Maybe customer number?
        customer_name = content[1] #assigned customer name to index 1 of the list
        expected_payment = float(content[2]) #assigned the expected payment to index 2 of the list
        actual_payment = float(content[3]) #assigned the actual payment to index 3 of the list

        if expected_payment != actual_payment: #if statment says if the customer did not pay 
            #the expected amount, then the program should print the statement specified.
            print(" {} paid ${:.2f}, but should have paid ${:.2f}".format( 
                customer_name, actual_payment, expected_payment) )
   
    payment_list.close() #close the file             


incorrect_payment_list("customer-orders.txt") #run the function with my text file

