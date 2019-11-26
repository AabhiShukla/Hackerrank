S = input().strip()
try:
    int_value = int(S)
    print(int_value)
except ValueError:
    print("Bad String")
