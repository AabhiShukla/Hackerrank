def check(num):
    if num % 2 == 0 and (num < 6 or num > 20):
        print("Not Weird")
    else:
        print("Weird")


if __name__ == '__main__':
    N = int(input())
    check(N)
