import termcolor2
def parameter():
    n = int(input("Enter Number: "))
    m = int(input("Enter Number: "))

    for i in range(n):
        print()
        for j in range(m):
            i = termcolor2.colored("#" , color="blue")
            j = termcolor2.colored("*" , color="yellow")
            print(i , j , end=" ")

print(parameter())

