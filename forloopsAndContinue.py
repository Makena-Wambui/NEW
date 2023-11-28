a = 0
for b in range(5):
    a = a + 2
    print(f"b: {b:d} a: {a:d}")
    if a == 6:
        continue
    print("This is how you illustrate continue.")
