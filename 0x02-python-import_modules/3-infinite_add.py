#!/usr/bin/python3

def main():
    from sys import argv
    
    sum = 0
    for i in range(1, len(argv)):
        sum = sum + int(argv[i])
    print(sum)


if __name__ == "__main__":
    main()
