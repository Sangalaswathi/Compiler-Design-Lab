def find_first(grammar, n, f, first):
    for i in range(n):
        if grammar[i][0] == f:
            if grammar[i][3].isupper():
                find_first(grammar, n, grammar[i][3], first)
            else:
                first[ord(f) - ord('A')] = grammar[i][3]

def main():
    n = int(input("Enter number of productions: "))
    grammar = []

    print("Enter grammar productions:")
    for _ in range(n):
        production = input().strip()
        grammar.append(production)

    first = [None] * 26  # Assuming non-terminals are A-Z

    for production in grammar:
        f = production[0]
        if production[3].isupper():
            find_first(grammar, n, f, first)
        else:
            first[ord(f) - ord('A')] = production[3]

    print("First function:")
    for i, f in enumerate(first):
        if f is not None:
            print(f"First({chr(ord('A') + i)}) = {f}")

if __name__ == "__main__":
    main()
