name = input("Enter your full name: ")
phone_num = input("Enter your Phone # : ")

length_Name = len(name)
length_Phone = len(phone_num)
find_o = name.find("o")
find_h = name.find("h")
find_rH = name.rfind('h')
upper_case = name.upper()
lower_case = name.lower()
capitalize_name = name.capitalize()
digts_n = name.isdigit()
digts_p = phone_num.isdigit()
alphab_n = name.isalpha()
alphab_p = phone_num.isalpha()
count_ph = phone_num.count("-")

print(f"length of name : {length_Name}")
print(f"length of phone # : {length_Phone}")
print(f"o's in name # : {find_o}")
print(f"h's in name # : {find_h}")
print(f"rH's in name # : {find_rH}")
print(f"Name's Uppercase : {upper_case}")
print(f"Name's Lowercase : {lower_case}")
print(f"Name's capitalize : {capitalize_name}")
if digts_p ==True:
    print (phone_num)
else:
    repl_p = phone_num.replace("-","")
    print(f"Phone Numbe : {repl_p}")

if digts_n == True:
    print("Name contains digits")
else:
    print(name)

if alphab_n == True:
    print("Name is correctly put")
else:
    print("name is wrong")

if alphab_p == True:
    print("Phone no. is worngly put")
else:
    print("Phone no.  is corect")


print(f"no of '-' in Phone no. {count_ph}")



