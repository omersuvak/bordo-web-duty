word =input("Bir kelime giriniz :")
word =word.replace(" ","")
word =word.lower()
temp =word[::-1]
if (word == temp):
    print("True")
else:
    print("False")