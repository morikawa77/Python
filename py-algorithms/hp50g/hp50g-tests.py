from hp50g import operation 

print("V Tests " + "-" * 20)
operation("V = 10 / 2")
# prints "V = 5"

operation("V = 10 * 2")
# prints "V = 20"

operation("V = 10 + 2")
# prints "V = 12"

operation("V = 10 - 2")
# prints "V = 8"



print("\nD Tests " + "-" * 20)


operation("10 = D / 2")
# prints "D = 20"

operation("10 = D * 2")
# prints "D = 5"

operation("10 = D + 2")
# prints "D = 8"

operation("10 = D - 2")
# prints "D = 12"



print("\nT Tests " + "-" * 20)


operation("50 = 10 / T")
# prints "T = 0.2"

operation("20 = 50 * T")
# prints "T = 0.4"

operation("120 = 20 + T")
# prints "T = 100"

operation("8 = 10 - T")
# prints "T = 2"

