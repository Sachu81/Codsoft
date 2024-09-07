
def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def multi(x, y):
    return x*y


def div(x, y):
    return x/y


print("Select Operation")
print(1, "+")
print(2, '-')
print(3, '*')
print(4, '/')

while True:
    choice = input("Enter Choice('1','2','3','4'):")
    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("Enter First Number:")
            num2 = float(input("Enter Second Number:")

            except ValueError:
                print("Invalid Input.")
                continue
            if choice == '1':
                print(num1,"+",num2,"=",add(num1,num2))
            if choice == '2':
                print(num1,"-",num2,"=",sub(num1,num2))
            if choice == '3':
                print(num1,"*",num2,"=",multi(num1,num2))
            if choice == '4':
                print(num1,"/",num2,"=",div(num1,num2))
            next_calculation = input("You Want Next Calculation? (yes/no):")
            if next_calculation == 'no':
                break
            else:
                print("Invakid Input")
