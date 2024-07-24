

def keep_dividing_recusrive(number, by):
    print("Caling keep_dividing_recursive : ")
    if number >= 1:
        print(f"Dividing {number} by {by} = ", number //by )
        number = number // by 
        keep_dividing_recusrive(number, by)
    else:
        print("We are done")

def keep_dividing_iterative(number, by):
    
    print("Caling keep_dividing_iterative : ")
    no_divisions = 0
    while number >= 1:
        print(f"Dividing {number} by {by} = ", number // by )
        no_divisions += 1 
        number = number // by

    print("We did ", no_divisions," total divisions")



number = 24
by =  2

keep_dividing_recusrive(24, 2)
keep_dividing_iterative(24, 2)
