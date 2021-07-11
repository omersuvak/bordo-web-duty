yazi =input("Cümle girin :")
dizi1 =yazi.split()
dizi2 =["ama", "ve", "veya", "göre", "ile", "yalnız", "ise", "ne", "nasıl", "ancak", "çünkü", "neden", "oysa", "için"]
for i in dizi1[::-1]:
    for j in dizi2:
        if (i == j):
            i = i[::-1]
    print(i,end=" ")



