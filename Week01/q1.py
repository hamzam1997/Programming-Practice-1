condition = "y"
strings = [];
while (condition == "y"):
    value = input("Enter your string. Input n to discontinue")
    if (value == "n"):
        condition = "n"
    else:
        strings.append(value)
size = len(strings)

max_string = 0
for i in strings:
    if len(i) > max_string:
        max_string = len(i)
asterisks = "* "*(max_string)
print(asterisks)
for i in strings:
    print("* " + i + (len(asterisks) - len(i)-4)*" "+"*")
print(asterisks)


    
        
