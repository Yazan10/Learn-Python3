class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print('The asnwer is: {}'.format(num1+num2))

    def subtract(self):
        print('The asnwer is: {}'.format(num1-num2))

    def muliply(self):
        print('The asnwer is: {}'.format(num1*num2))

    def divide(self):
        print('The asnwer is: {}'.format(num1//num2))

num1=float(input('Type the first number: '))
num2=float(input('Type the second number: '))
cal=calculator(num1,num2)
cal.add()
p