# kullanıcıdan 5 sayı alan ve bu sayılardan sadece 
# 18'den büyük olanları toplayan kodu yazın (for döngüsü)
toplam = 0
for x in range(5):
    girilen_sayi = int(input("lütfen bir sayi girin:"))
    if girilen_sayi <25 and girilen_sayi >10:
        toplam = toplam + girilen_sayi
        print("")

print(toplam)