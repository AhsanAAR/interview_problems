# python dictionary. Stores key value pairs. Provides O(1) average access times using hashmaps.
# similar to using indexes in list, we can use key here. Key can be anythingß
wallet_dict = {
    'Alice': 2,
    'Bob': 4,
    'Charlie': 0,
}

# O(1) average access
print(f"Alice's wallet contains {wallet_dict['Alice']} dollars")
print(f"Bob's wallet contains {wallet_dict['Bob']} dollars")
print(f"Charlie's wallet contains {wallet_dict['Charlie']} dollars")

# looping using keys
for key in wallet_dict:  # same as wallet_dict.keys()
    wallet_dict[key] += 1

print("modified wallet", wallet_dict)

print('\n', 'looping using values')
total_money = 0
for value in wallet_dict.values():
    total_money += value

print(f"we have {total_money} dollars in wallet")

print('\n', 'looping using items')
for key, value in wallet_dict.items():
    print(f"{key} has {value} dollars")
