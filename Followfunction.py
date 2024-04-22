def find_follow(prods):
    follow = {}
    for i in range(len(prods)):
        for j in range(3, len(prods[i])):
            if prods[i][j].isupper():
                if j == len(prods[i]) - 1:
                    if prods[i][j] not in follow:
                        follow[prods[i][j]] = set()
                    follow[prods[i][j]].add(prods[i][0])
                else:
                    if not prods[i][j + 1].isupper() and prods[i][j + 1] != '\0':
                        if prods[i][j] not in follow:
                            follow[prods[i][j]] = set()
                        follow[prods[i][j]].add(prods[i][j + 1])
                    if prods[i][j + 1].isupper():
                        k = i
                        l = j
                        while k < len(prods):
                            if prods[k][0] == prods[i][j + 1]:
                                if not prods[k][3].isupper():
                                    if prods[i][j] not in follow:
                                        follow[prods[i][j]] = set()
                                    follow[prods[i][j]].add(prods[k][3])
                                    break
                                else:
                                    i = k
                                    j = 2
                                    continue
                            k += 1
                        i = i
                        j = l
    return follow

if __name__ == "__main__":
    np = int(input("Enter number of productions: "))
    prods = []
    print("Enter grammar productions:")
    for _ in range(np):
        prods.append(input().strip())

    print("Follow function:")
    follow_set = find_follow(prods)
    for key, value in follow_set.items():
        print(f"Follow({key}) = {' '.join(sorted(value))}")
