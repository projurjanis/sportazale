max_ietilpiba = 20
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



while restart == "y":
    i=1
    id=1
    izvele0 = int(
        input(
            "_____________________________________________________________\n1.Veikt rezervāciju\n2.Atcelt rezervāciju\n3.Pamest lietotni\nIevadi skaitli!\n"
        ))
    if izvele0 == 3:
        restart = "n"
    if izvele0 == 1:
        print("_____________________________________________________________\nIzvēlies dienu!")
        for z in (pieejamas_dienas):
          print(str(i)+"."+z)
          i+=1
          if i==len(pieejamas_dienas)+1:
            print(str(i)+".atpakaļ")
        izvele1=int(input("Ievadi skaitli!\n"))
        if izvele1==len(pieejamas_dienas)+1:
          continue
        elif izvele1>len(pieejamas_dienas):
          print("_____________________________________________________________\nTādas izvēles nepastāv, lūdzu sāciet pa jaunam.")
          continue       
        else:
          i=0
          diena=izvele1
          print("_____________________________________________________________")
          for z in (dict_laiki[diena]):
            i+=1
            print(str(i)+"."+z)
            if i==len(dict_laiki[diena]):
              i+=1
              print(str(i)+".atpakaļ")
            izvele2=int(input("Ievadi skaitli!\n"))
            if izvele2==i:
              continue
            elif izvele2>i:
              print("_____________________________________________________________\nTādas izvēles nepastāv, lūdzu sāciet pa jaunam.")
              continue
            else:
              laiks=izvele2
              vards=("Ievadi savu pilno vārdu un uzvārdu:\n")
              print(f"Paldies par reģistrāciju! Jūsu reģistrācijas ID ir {id}")
              continue
              




