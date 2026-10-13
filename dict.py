stu={
    "name ":"Madhu Vinay",
    "age ": 23,
    "city":"Amaravathi"
}

print(stu["name "])
# print(stu[0])
# safest method to check for keys ,it returns none if key is not present instead of errorerror
print(stu.get("name1"))#it i will not give the error but give the none 

# updating the values

stu["city"]="Hyderabad"
print(stu["city"])

# adding new key value pairs
stu["phone_number"]=6301857835
print(stu)
