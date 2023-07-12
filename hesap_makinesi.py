import random
from os import name, system
from time import sleep
from math import sqrt

while True:
    x = random.randint(2, 4)
    
    def out():
        for i in range(x):
            print("Coming Out.")
            sleep(0.2)
            system("clear") if name == "posix" else system("cls")
            print("Coming Out..")
            sleep(0.2)
            system("clear") if name == "posix" else system("cls")
            print("Coming Out...")
            sleep(0.2)
            system("clear") if name == "posix" else system("cls")

    def cls():
        system("clear") if name == "posix" else system("cls")

    def hesap():
        for i in range(x):
            print("Hesaplanıyor.")
            sleep(0.2)
            system("clear") if name == "posix" else system("cls")
            print("Hesaplanıyor..")
            sleep(0.2)
            system("clear") if name == "posix" else system("cls")
            print("Hesaplanıyor...")
            sleep(0.2)
            system("clear") if name == "posix" else system("cls")

    def b():
        for i in range(x):
            print("Lütfen Belirtilen İşlemlerden Birini Giriniz.")
            sleep(0.2)
            system("clear") if name == "posix" else system("cls")
            print("Lütfen Belirtilen İşlemlerden Birini Giriniz..")
            sleep(0.2)
            system("clear") if name == "posix" else system("cls")
            print("Lütfen Belirtilen İşlemlerden Birini Giriniz...")
            sleep(0.2)
            system("clear") if name == "posix" else system("cls")
        

    cls()


    a = input("""
    (1) Toplama
    (2) Çıkarma
    (3) Çarpma
    (4) Bölme
    (5) Üs alma
    (6) Karekök alma
    (7) Faktöriyel alma
    (q) Çıkış

    İşleminizi giriniz : 
    """)
    
    if a == "q":
        out()
        break

    

       
    if a == "1":
        print("Toplama")
        
    elif a == "2":
        print("Çıkarma")
        
    elif a == "3":
        print("Çarpma")
        
    elif a == "4":
        print("Bölme")

    elif a == "5": 
        print("Üs Alma")

    elif a == "6":
        print("Karekök Alma")
        
    elif a == "7":
        print("Faktöriyel Alma")


    else:
        b()
        cls()
        continue

    cls()
        

    if a == "1":
        b = int(input(" 1. Sayı : " ))
        c = int(input(" 2. Sayı : " ))
        cls()
        hesap()
        d = b + c
        
    elif a == "2":
        b = int(input(" 1. Sayı : " ))
        c = int(input(" 2. Sayı : " ))
        cls()
        hesap()
        d = b - c
        
    elif a == "3":
        b = int(input(" 1. Sayı : " ))
        c = int(input(" 2. Sayı : " ))
        cls()
        hesap()
        d = b * c
        
    elif a == "4":
        b = int(input(" 1. Sayı : " ))
        c = int(input(" 2. Sayı : " ))
        cls()
        hesap()
        d = b / c

    elif a == "5":
        b = int(input(" 1. Sayı : " ))
        c = int(input(" 2. Sayı : " ))
        cls()
        hesap()
        d = b**c

    elif a == "6":
        b = int(input(" Karekökünün Alınması İstenen Sayı : " ))
        cls()
        hesap()
        d = sqrt(b)
        
    elif a == "7":
        b = int(input("Faktöriyeli alınması istenen sayıyı giriniz:"))
        cls()
        hesap()

        d = 1

        if b >= 0:
            for i in range(1 , b + 1):
                d = d * i
  
        
    print("Cevabınız :", d)
    sleep(3)
    cls()
            

