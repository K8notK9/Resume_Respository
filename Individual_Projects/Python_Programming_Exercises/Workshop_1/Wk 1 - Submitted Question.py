def combo_string(a, b):
    short = min(a, b, key=len)
    long = max(a, b, key=len)
    return short + long + short

a = input("Enter the A: ")
b = input("Enter the B: ")
print(combo_string(a, b))