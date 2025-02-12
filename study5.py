num = 1

try:
    print("1")
    
    if num == 1:
        raise KeyboardInterrupt

    print("2")
except KeyboardInterrupt:
    print("4")
else:
    print("5")
finally:
    print("6")
    
print("7")