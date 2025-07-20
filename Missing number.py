giris_sayi=int(input())
if 2<=giris_sayi<=2*10**5:
 eded_siyahisi=[]
 for i in range (giris_sayi-1):
     eded=int(input("Ededi daxil edin: "))
     if 0<eded<=giris_sayi:
      eded_siyahisi.append(eded)
 if len(eded_siyahisi)==(giris_sayi-1):
    t=giris_sayi 
    for j in range (giris_sayi):
      t=t-1
      if t not in eded_siyahisi:
         break
      print(t)
 else:
    print("Xais edirik araliga daxil eded daxil edin.") 
else:
  print("Limit kecilibdir.")       
               

