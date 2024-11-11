def combine_strings(a, b):
    if not a:
        a = '@'
    if not b:
        b = '@'

    result = a[0] + b[-1]
    print(result)


# Example usage:
a_input = input("Enter the first string: ")
b_input = input("Enter the second string: ")
print ("The resulting string is: " ), combine_strings(a_input, b_input)
