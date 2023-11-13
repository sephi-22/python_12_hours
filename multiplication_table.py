#This is a program to write a multiplication table using loops
def print_multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1,11):
            print (f"{i} times {j} is {i*j}")
        print("")


#test
print_multiplication_table(5)