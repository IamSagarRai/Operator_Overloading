class Number:
    def __init__(self, num):
        self.num = num


    def __add__(self, num2):
        print("Lets add qwertyuiop")
        return self.num + num2.num

    def __mul__(self, num2):
        print("Lets multiply asdfghjkl")
        return self.num * num2.num

    

num1 = Number(4)
num2 = Number(6)
sum = num1 + num2
mul = num1 * num2
print(sum)
print(mul)


