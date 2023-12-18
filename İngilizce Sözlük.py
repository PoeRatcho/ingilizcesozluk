sözlük = {}
while True:

    print("""
[1] YENİ KELİME EKLEME
[2] KELİME ÖĞRENME
[3] KELİME SİLME
[Q] ÇIKIŞ
""")

    veri = input("Yapmak İstediğiniz İşlemi Seçiniz... : ")

    if veri == "1":
        kelime = input("Eklemek İstediğiniz Kelimeyi Yazınız: ")
        anlamı = input("Kelimenin Anlamını Giriniz: ")
        print(f"Eklenen Kelime: {kelime}" , end = '\n' f"Anlamı: {anlamı}")
        sözlük.setdefault(kelime,anlamı)
    elif veri == "2":
        sor = input("Aranan Anahtarı giriniz: ")
        if sor in sözlük.keys():
            print(sözlük.get(sor))
            print(f"Aranan Kelime: {sor}" , end = '\n' f"Anlamı: {anlamı}")
        else:
            print("Hata")
    elif veri == "3":
        silme = input("Hangi Kelimeyi Silmek İstiyorsunuz ? (İngilizce Yazınız): ")
        if silme in sözlük.keys():
            sözlük.pop(silme)
            print("Kelime Silindi...")
        else:
            print("Böyle Bir Kelime Zaten Yok...")
    elif veri == "q" or veri == "Q":
        print("Çıkış Yapıldı...")
        break
    else:
        print("Hatalı Tuşlama Yaptınız , Tekrar Deneyiniz...")
        break
