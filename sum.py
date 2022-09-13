num = int(input("Enter a number: "))
m=int(input("end number"))
def sum(n):
    if n <= m:
        return n
    else:
        return n + sum(n-1)
print("The sum is: ", sum(num))
