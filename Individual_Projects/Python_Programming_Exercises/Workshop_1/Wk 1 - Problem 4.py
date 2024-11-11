def count_clump(lst):
    count = 0
    prev_index = None
    for i, element in enumerate(lst):
        if prev_index is None:
            prev_index = i
        else:
            if lst[prev_index] == element:
                if i == prev_index + 1:
                    count += 1
                else:
                    prev_index = i
    return count
def main():
    elements_str = input ("Enter elements separated by space: ")
    elements = elements_str.split
    count = count_clump(elements)
    print("The number of clumps in the list is: ", count)

if __name__ == "__main__":
    main()