
def time_to_seconds(hours, minutes, seconds):
    return seconds + 60*minutes + 60*60*hours

def main():
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))
    tsl = time_to_seconds (hours, minutes, seconds)
    print(f"Equivalent time: ", tsl);


if __name__ == "__main__":
    main()