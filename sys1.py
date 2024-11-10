import sys

print("Type something... ")
for line in sys.stdin:
    if line.strip() == 'exit':
        break
    sys.stdout.write(f">> {line}")


"""
└─$ python3 sys1.py 
Type something... 
Hi
>> Hi
Hello  
>> Hello
exit
"""