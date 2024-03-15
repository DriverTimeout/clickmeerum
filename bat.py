# Function definitions
def highnum(a, b, c, d, e):
    return max(a, b, c, d, e)

def lownum(a, b, c, d, e):
    return min(a, b, c, d, e)

def main():
    # User input
    a = int(input("Enter the value for a ==> "))
    b = int(input("Enter the value for b ==> "))
    c = int(input("Enter the value for c ==> "))
    d = int(input("Enter the value for d ==> "))
    e = int(input("Enter the value for e ==> "))

    # Function calls
    tempH = highnum(a, b, c, d, e)
    tempL = lownum(a, b, c, d, e)

    # Output
    print("The highest number is ==> ", tempH)
    print("The lowest number is ==> ", tempL)

if __name__ == "__main__":
    main()
