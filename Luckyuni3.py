def int_check(question):

    error = "Please enter a number that is more than 0 and less than or equal to 10"

    valid = False
    while not valid:

        try:
            # Ask question
            response = int(input(question))

           if 0 < response <= 10:

            return  response

           # If response is invalid, display error
           else:
             print (error)

        except ValueError:
            print(error)

amount = int_check("How much do you want to play with? ")
price = amount

