 str = str (input("Enter comma separated integers: "))
list = str.split (",")
li = []
for i in list:
	li.append(int(i))
for dig in li:
    if dig%2!=0:
        print(dig)
