bar = 1024

print(f"[bar] : {bar}, [data type of bar] : {type(bar)}")

bar_byte = bar.to_bytes(4, 'big')

print(f"[bar_byte] : {bar_byte}, [data type of bar_byte/] : {type(bar_byte)}")