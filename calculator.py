print(20*"=")
print('Simple Calculator')
print(20*"=")

num_1 = float(input("input the first number = "))
operator = input("input your operator +,-,x,/ =")
num_2 = float(input("input the second number = "))

if operator=="+":
    answer = num_1 + num_2
    print(f"Your answer : {answer}")
elif operator=="-":
    answer = num_1 - num_2 
    print(f"Your answer : {answer}")
elif operator=="*" or operator == "x":
    answer = num_1 * num_2 
    print(f"Your answer : {answer}")
elif operator=="/":
    answer = num_1 / num_2 
    print(f"Your answer : {answer}")

else:
    print("\nYour input is wrong please try again\n")
print("End of the program")