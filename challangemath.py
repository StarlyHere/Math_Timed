import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12




def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
print("ARE YOU READY?")
print(" ")
print("Select your level! 1/2/3")
level = int(input("Enter you Level: "))
if level == 1:
    total = 5
elif level ==2:
    total =10
elif level==3:
    total=20
input("Press enter to start!")
print("----------------------")

start_time = time.time()


for i in range(total):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")
