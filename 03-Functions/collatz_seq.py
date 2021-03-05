import sys, time

def main():
    print("Enter a number: ")

    try:
        n = int(input())
    except ValueError:
        print("Error: must be an integer")
        sys.exit()

    while n != 1:
        n = collatz(n)


def collatz(number):
    if number % 2 == 0:
        res = number // 2
    else:
        res = 3 * number + 1
    print(res)
    return res

if __name__ == "__main__":
    main()


