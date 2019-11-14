def cons(n):
    max_length=0
    c=str(bin(n))
    c=c[2:]
    binary_list=(c.split("0"))
    for i in binary_list:
        if len(i) > max_length:
            max_length = len(i)
    
    return (max_length)

n = int(input())
print (cons(n))
