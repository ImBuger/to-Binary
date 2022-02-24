print("""***********************************************
İKİLİK TABANA ÇEVİRME SİHİRBAZI'NA HOŞGELDİNİZ!' 
***********************************************  """) #isteğe bağlı olarak başlık
sayı = int(input("Lütfen Sayı giriniz:")) #kullanıcıdan sayı girdisi alınır
bolum = sayı // 2 #bölüm tanımlanır (ondalık sayıdan binarye çevirme yöntemi esas alınır, 2'e bölünür)
kalan = sayı % 2 #kalan tanımlanır
ikilik = str(kalan) #ikilik değişkeni tanımlanır
while(bolum != 0): #döngü 'while' ile kurulur. 0 olmadığı sürece devam eder.
    islem = bolum #işlem atanır
    bolum = islem// 2 #ondalık sayıyı binarye çevirmede sürekli 2'ye bölme işlemi burada uygulanır
    kalan = islem % 2 #kalanın mod 2'si alınır
    ikilik = ikilik + str(kalan) #ikilik değişkeni döngü içinde kalanın string şekliyle toplanır
kacbit = len(ikilik) #ben daha farklı bir gösterim olmasını tercih ettiğim için kaç bit olduğunu da göstermek istedim. "kacbit" isimli değişkeni tanımladım ve "ikilik" değişkeninin uzunluğuna göre bit sayısını gösterdim. len fonksiyonu kullandım.
print("GİRDİĞİN",sayı,"SAYISI SİHİRBAZDAN",kacbit,"BİT",",",ikilik[::-1],"İKİLİK FORMUNDA ÇIKMIŞTIR!") #ve yazdırdım.
print("-_-") #imzam

