#dictionary slicing

d1= { "1":"asd" ,"2":"abcd" , "3": [3,6,9,12], "4": "avidd"}
print(d1)

d1 ["5"]="(23,32,12)"
print(d1)

print(d1.keys())

print(d1.items())

del d1["1"]
print(d1)

print(d1.get("2"))

d1.update({"1":"aqwq"})
print(d1)
