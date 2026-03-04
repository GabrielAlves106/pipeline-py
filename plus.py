import sys

def plus(a : int, b : int) -> int:
    assert a != 0 or b != 0 
    return a + b

if __name__ == "__main__":
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    print(plus(num1, num2))