a=int(input("Sisestage 1 arv: "))
b=int(input("Sisestage 2 arv: "))
c=input("Sisestage 3 arv: ")
if c == "+": 
       print(a, "+", b, "=", a+b )
elif c == "-":
      print(a, "-", b, "=", a-b)
elif c == "*":
      print(a, "*", b, "=, a*b")
elif c == "/":
      print(a, "/", b, "=", a/b)
else:
      print("Tundmatud operatsioon ")

      
      
      from Modul import *
while True:
    print("Funktsioonid".center(50,"+"))
    v=input("arithmetic- A,\nis_year_leap-Y")
    v=input()
    if v.upper()=="A":
        arv1=float(input("Arv 1:"))
        arv2=float(input("Arv 2:"))
        sym=input("Tehe:")
        rezult=arithmetic(arv1,arv2,sym)
        print(rezult)
    elif v.upper()=="Y":
        rezult=is_year_leap(int(input("Sisesta aasta: ")))
        print

        
        
        def square(a):
	p = 4*a
	s = a*a
	d = (a**2) / 2
	d = d**0.5
	
	k = (p, s, d)
	
	return k
	
print(square(16))


def season(moth):

    if month == 12 or month < 3:
        return "Talv"
    elif month == 3 or month < 6:
        return "Kevad"
    elif month == 6 or month < 9:
        return "Suvi"
    else:
        return "Sügis"



month = input("Sisestage kuu(arv):")

while True:
    if not month.isdigit():
        print("Viga!")
        print("Sisestage ainult täis arv.")
        month = input("Sisestage kuu(arv):")
        continue
    else:
        break

month = int(month)
while True:
    if month == 0:
        print("Sellist kuud ei ole")
        print("Sisestage ainult täis arv.")
        month = input("Sisestage kuu(arv):")
        continue
    else:
        break

kuu = int(kuu)

answer = season(month)
print(vastus)


def bank(a:float,years:int):

    """Paneme raha saldole ja ootame n arv aastaid

    :param float a:Esimene arv

    :param float years: Teine arv

    :rtype float

    """

    for _ in range(years):

        a=((1.1*1/100)*a)*100

    print("Teie tasakaalu:",a)

    return("")



def season(kuu):

    if kuu == 12 or kuu < 3:
        return "Talv"
    elif kuu == 3 or kuu < 6:
        return "Kevad"
    elif kuu == 6 or kuu < 9:
        return "Suvi"
    else:
        return "Sügis"



kuu = input("Sisestage kuu(arv):")

while True:
    if not kuu.isdigit():
        print("Viga!")
        print("Sisestage ainult täis arv.")
        kuu = input("Sisestage kuu(arv):")
        continue
    else:
        break

kuu = int(kuu)
while True:
    if kuu == 0:
        print("Sellist kuud ei ole")
        print("Sisestage ainult täis arv.")
        kuu = input("Sisestage kuu(arv):")
        continue
    else:
        break

kuu = int(kuu)

vastus = season(kuu)
print(vastus)



def is_year_leap(year):
    """
    Võtab argumendi: aasta järg
    Tagastab, kui liigaasta on Tõene, vastasel juhul False
    """
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True
def date(day, month, year):
    """
    Aktsepteerib argumente: päev, kuu, aasta
    Tagastab väärtuse: kui kuupäev on õige - True, vaid - False
    """
    # Määrame päevade arvu kuudes mitteliigaastal
    set_months = {1: 31,
                  2: 28,
                  3: 31,
                  4: 30,
                  5: 31,
                  6: 30,
                  7: 31,
                  8: 31,
                  9: 30,
                  10: 31,
                  11: 30,
                  12: 31}
    # Kontrollime, kas aasta ja kuu on õigesti seatud
    if year > 0 and (month >= 1 and month <= 12):
        # Veebruari päevade arvu muutmine liigaaastatel
        if month == 2 and is_year_leap(year) == True:
            set_months[2] = 29
        # Kontrollime, kas päev on õigesti seatud
        if day in range(1, set_months[month]+1):
            return True
        else:
            return False
    else:
        return False
# Test
print(date(31, 12, 2020)) # õige kuupäev
print(date(1, 0, 2000)) # Kuu väljaspool ulatust
print(date(1, 1, 0)) # aasta väljaspool ulatust
print(date(29, 2, 2000)) # 29. veebruar on liigaasta
print(date(29, 2, 1900)) # 29. veebruar on tavaline aasta


def str_xor(string,key):

