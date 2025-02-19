bar = {"name" : "wonjun", "age" : 24, "phone" : 1234, "email" : "example@example.com"}

for key, value in bar.items():
    print(f"key : {key}, value : {value}")
    
print(bar['name'])

del bar['name']

print(bar)

for key in bar.keys():
    print(key)
    
for value in bar.values():
    print(value)
    
for key, value in bar.items():
    print(key, value)