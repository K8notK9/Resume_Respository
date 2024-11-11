def calculate_change(cost):
    # Convert cost to cents
    cost_cents = int(cost * 100)

    # Initialize coin values
    coin_values = [50, 20, 10, 5, 1]
    coin_counts = [0] * len(coin_values)

    # Calculate the number of each coin
    for i, coin in enumerate(coin_values):
        coin_counts[i] = cost_cents // coin
        cost_cents %= coin

    # Print the results
    print(f"50 cent coins: {coin_counts[0]}")
    print(f"20 cent coins: {coin_counts[1]}")
    print(f"10 cent coins: {coin_counts[2]}")
    print(f"5 cent coins: {coin_counts[3]}")
    print(f"1 cent coins: {coin_counts[4]}")

# Example usage
item_cost = float(input("Enter the cost of the item in cents (<= 100): "))
calculate_change(item_cost)
