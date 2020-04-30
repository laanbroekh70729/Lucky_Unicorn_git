def int_check(question):

    error = "Please enter a number that is more than 0 and less than or equal to 10"

    valid = False
    while not valid:

        try:
            response = float(input(question))



        except ValueError:
            print(error)
