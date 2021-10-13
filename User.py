from main import calculator

cal=calculator()
print("Enter 1 to addition")
print("Enter 2 to subtraction")
print("Enter 3 to multiply")
print("Enter 4 to division")
print("Enter 0 to exit")
inp=input("Enter Operation = ")
while(inp!="0"):
    first = int(input("Enter First Number = "))
    second = int(input("Enter Second Number = "))
    if(inp=="1"):
        print(f"Output:  {cal.add(first, second)}")
    elif(inp=="2"):
        print(f"Output:  {cal.sub(first, second)}")
    elif(inp=="3"):
        print(f"Output:  {cal.mul(first, second)}")
    elif(inp=="4"):
        print(f"Output:  {cal.div(first, second)}")
    inp=input("Enter Operation = ")


