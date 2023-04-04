with open("currency_data.txt") as f:
    lines = f.readlines()

currency_dict = {}
for line in lines:
    parsed = (line.split("\t"))
    # print(parsed[0])
    # print(parsed[1])
    # print(parsed[2])
    currency_dict[parsed[0]] = parsed[1]
    
# print(currency_dict)

user_rs = int(input("enter No. of Rs: "))
[print(itms) for itms in currency_dict.keys()]
user_name = input("enter country name from above available options: ")

if currency_dict.get(user_name) != None:
    print(currency_dict.get(user_name))
    print(f"{user_rs} Rs in {user_name} {user_rs*float(currency_dict.get(user_name))}")
 