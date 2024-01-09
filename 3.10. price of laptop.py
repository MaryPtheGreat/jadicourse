
def find_laptops(n, laptops):
    for i in range(n):
        for j in range(n):
            price1, quality1 = laptops[i]
            price2, quality2 = laptops[j]

            if price2 < price1 and quality2 > quality1:
                return "happy irsa"

    return "poor irsa"


n = int(input())
laptops = []
for _ in range(n):
    price, quality = map(int, input().split())
    laptops.append((price, quality))

result = find_laptops(n, laptops)
print(result)
