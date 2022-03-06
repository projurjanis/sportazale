f = open("id.txt","r")
id=int(f.readline())
f.close()

max_ietilpiba = 5

restart = "y"

pieejamas_dienas = [
    "pirmdiena", "otrdiena", "trešdiena", "ceturtdiena", "piektdiena",
    "sestdiena", "svētdiena"
]
pieejamie_laiki_1=["9:00-10:30","10:30-12:00","12:00-13:30","13:30-15:00","15:00-16:30","16:30-18:00","18:00-19:30","19:30-21:00"]
pieejamie_laiki_2=["9:00-10:30","10:30-12:00","12:00-13:30","13:30-15:00","15:00-16:30","16:30-18:00","18:00-19:30","19:30-21:00"]
pieejamie_laiki_3=["9:00-10:30","10:30-12:00","12:00-13:30","13:30-15:00","15:00-16:30","16:30-18:00","18:00-19:30","19:30-21:00"]
pieejamie_laiki_4=["9:00-10:30","10:30-12:00","12:00-13:30","13:30-15:00","15:00-16:30","16:30-18:00","18:00-19:30","19:30-21:00"]
pieejamie_laiki_5=["9:00-10:30","10:30-12:00","12:00-13:30","13:30-15:00","15:00-16:30","16:30-18:00","18:00-19:30","19:30-21:00"]
pieejamie_laiki_6=["9:00-10:30","10:30-12:00","12:00-13:30","13:30-15:00","15:00-16:30","16:30-18:00","18:00-19:30","19:30-21:00"]
pieejamie_laiki_7=["9:00-10:30","10:30-12:00","12:00-13:30","13:30-15:00","15:00-16:30","16:30-18:00","18:00-19:30","19:30-21:00"]
dict_laiki={
  1:pieejamie_laiki_1,
  2:pieejamie_laiki_2,
  3:pieejamie_laiki_3,
  4:pieejamie_laiki_4,
  5:pieejamie_laiki_5,
  6:pieejamie_laiki_6,
  7:pieejamie_laiki_7
}
dict_faili={
  1:"pirmdiena.txt",
  2:"otrdiena.txt",
  3:"tresdiena.txt",
  4:"ceturtdiena.txt",
  5:"piektdiena.txt",
  6:"sestdiena.txt",
  7:"svetdiena.txt"
}


dict_ietilpiba={
  1:[0,0,0,0,0,0,0,0],
  2:[0,0,0,0,0,0,0,0],
  3:[0,0,0,0,0,0,0,0],
  4:[5,5,5,5,5,5,5,5],
  5:[0,0,0,0,0,0,0,0],
  6:[0,0,0,0,0,0,0,0],
  7:[0,0,0,0,0,0,0,0]
}

while restart == "y":
  nepieejamas_dienas=[]
  i=1
  for i in range(1, 8):
    with open(dict_faili[i], "r") as f:
      lines = f.readlines()
    with open(dict_faili[i], "r") as f:
      for line in lines:
        saraksts = line.split()
        if len(saraksts)<4:
          continue
        else:
          laikaid = int(saraksts[3])
          (dict_ietilpiba[i])[laikaid-1]+=1
  for i in range(1,8):
    skaits_pilns=0
    for y in range(8):
      if (dict_ietilpiba[i])[y]>=max_ietilpiba:
        skaits_pilns+=1
        if skaits_pilns==8:
          nepieejamas_dienas.append(i)
  izvele0 = int(
      input(
        "_____________________________________________________________\n1.Veikt rezervāciju\n2.Atcelt rezervāciju\n3.Pamest lietotni\nIevadi skaitli!\n"
        ))
  if izvele0 == 3:
      restart = "n"
  if izvele0 == 1:
    i=1
    print("_____________________________________________________________\nIzvēlies dienu!")
    izlaistas_dienas=[]
    for z in (pieejamas_dienas):
      if i not in nepieejamas_dienas:
        print(str(i-len(izlaistas_dienas))+"."+z)
        i+=1
      else:
        izlaistas_dienas.append(i)
        i+=1
      if i==len(pieejamas_dienas)+1:
        print(str(i-len(izlaistas_dienas))+".sākums")
    izvele1=int(input("Ievadi skaitli!\n"))
    if izvele1==i-len(izlaistas_dienas):
      continue
    elif izvele1>len(pieejamas_dienas)-len(izlaistas_dienas):
      print("_____________________________________________________________\nTādas izvēles nepastāv, lūdzu sāciet pa jaunam.")
      continue       
    else:
      izlaistie_laiki=[]
      nepieejamie_laiki=[]
      i=0
      for i in range(1,izvele1+1):
        if i in izlaistas_dienas:
          izvele1+=1
      diena=izvele1
      for i in range(8):
        if dict_ietilpiba[diena][i]>=max_ietilpiba:          
          nepieejamie_laiki.append(i+1)
      print("_____________________________________________________________")
      i=1
      
      for z in dict_laiki[diena]:
        if i not in nepieejamie_laiki:
          print(str(i-len(izlaistie_laiki))+"."+z)
          i+=1
        else:
          izlaistie_laiki.append(i)
          i+=1
        if i==len(dict_laiki[diena])+1:
          print(str(i-len(izlaistie_laiki))+".sākums")
      izvele2=int(input("Ievadi skaitli!\n"))
      if izvele2==i-len(izlaistie_laiki):
        continue
      elif izvele2>i-len(izlaistas_dienas):
        print("_____________________________________________________________\nTādas izvēles nepastāv, lūdzu sāciet pa jaunam.")
        continue
      else:
        for i in range(1,izvele2+1):
          if i in izlaistie_laiki:
            izvele2+=1
        laiks=izvele2
        print("_____________________________________________________________")
        vards=input("Ievadi savu pilno vārdu un uzvārdu:\n")
        personas_kods=input("Ievadi savu personas kodu (tiks izmantots rezervācijas atcelšanai):\n")
        print(f"Paldies par reģistrāciju! Jūsu reģistrācijas ID ir {id+1}. Pierakstiet to, ja nu gadījumā jāatceļ rezervācija!")
        id+=1
        f=open("id.txt","w")
        f.write(str(id))
        f.close()
        f=open(dict_faili[diena],"a")
        f.write(str(id)+" "+personas_kods+" "+str(diena)+" "+str(laiks)+" "+str(pieejamas_dienas[diena-1])+" "+str(dict_laiki[diena][laiks-1])+" "+vards+"\n")
        f.close()
        continue
  if izvele0 == 2:
    idievade=input("Ievadi savu personas kodu, lai atceltu rezervāciju.\nJa vēlies atpakaļ, rakstiet burtu x: ")
    if idievade=="x":
      continue
    vai_ir = False
    skaits = 0
    for i in range(1,8):
      with open(dict_faili[i], "r") as f:
        lines = f.readlines()
      with open(dict_faili[i], "r") as f:
        for line in lines:
          saraksts=line.split()
          if saraksts[1]==str(idievade):
            skaits+=1
            vai_ir = True
    if vai_ir and skaits==1:
      for i in range(1,8):
        with open(dict_faili[i], "r") as f:
          lines = f.readlines()
        with open(dict_faili[i], "w") as f:
          for line in lines:
            saraksts=line.split()
            if saraksts[1]!=str(idievade):
                f.write(line)
      print("Paldies, jūsu rezervācija ir atcelta!")
    elif vai_ir and skaits>1:
      idievade2=input("Ievadi savu rezervācijas ID, uz doto personas kodu ir vairākas rezervācijas:\n")
      for i in range(1,8):
        with open(dict_faili[i], "r") as f:
          lines = f.readlines()
        with open(dict_faili[i], "w") as f:
          for line in lines:
            saraksts=line.split()
            if saraksts[0]==str(idievade2) and saraksts[1]==str(idievade):
              continue
            else:
              f.write(line)
    else:
      print("Rezervācija ar izvēlēto personas kodu neeksistē!")
for i in range(1,8):
  print(dict_ietilpiba[i])