word = str(input("Enter a word:\n"))
rev=""


for ch in word:
    rev = ch+rev


print("Palindrome"if word ==rev else"Not palindrome")
