for item in range(5):  # outer loop / loop
    for num in range(10):  # inner loop / loop anidado
        print(f"{item} x {num} = {item * num}")
        if num == 9:
            print("-" * 20)
