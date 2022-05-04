
def function(x,y):
    return 2*x-y
    pass

def sigma(start, end,y):
    toplam=0
    for i in range(start,end+1):
        toplam+=function(i,y)
    return toplam

control=False

sonuc=int(input("sigması buluncak sayı giriniz:"))
print("Sonuçlar:")
for i in range(1,10000):
    for j in range(1,1000):
        if (sigma(1,j,i)>sonuc):
            break
        elif(sigma(1,j,i)==sonuc):
            print("1 den",j,"2 * x -",i,"sonuc",sigma(1,j,i))
            break
        

