
lst = [99, 23, 64, 12, 656]

firs_lar = lst[0]               # as we don't know the First or Second Largest we have defined as the first element 🥴
sec_lar = lst[0] 

for i in range(1, len(lst)):
    if lst[i] > firs_lar:
        sec_lar = firs_lar
        firs_lar = lst[i]

    elif lst[i] > sec_lar:
        sec_lar = lst[i]


print(firs_lar, sec_lar)