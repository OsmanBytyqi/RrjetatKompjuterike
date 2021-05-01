import socket
import random
import datetime

import sys
from termcolor import colored
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint

from pyfiglet import figlet_format
from pyfiglet import Figlet
print_red=lambda x:cprint(x,'red')
print_green=lambda x:cprint(x,'green')


f=Figlet(font='slant')


serverName = 'localhost'
serverPort = 14000

serveri = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serveri.bind((serverName, serverPort))
print_green("===============================================================================")
print((colored(figlet_format("SERVERI-UDP!"), color="green")))
print_green("===============================================================================")
print("Serveri eshte duke pritur kerkesen nga klienti ...")






def IP(para):
    return para[0]

def NRPORTI(para):
    return para[1]

def NUMERO(para):
    zanoret = 0
    bashketingelloret = 0
    
    for z in para:
      if z in ['a','e','ë','i','o','u','y','A','E','Ë','I','O','U','Y']:
            zanoret += 1
      elif z in ['b', 'c', 'ç', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z',
                   'B', 'C', 'Ç', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z']:
            bashketingelloret += 1
    x = "Zanore :" + str(zanoret)
    y = "Bashketingellore : " + str(bashketingelloret)
    return x, y

def ANASJELLTAS(para):
    fjala = ""
    for i in para:
        fjala = i + fjala
    return fjala


def PALINDROME(para):
    if (para == para[:: - 1]):
        x = "Teksti eshte polindrom"
    else:
        x = "teksti nuk eshte polindrom"
    y = str(x)
    return y


def KOHA():
    from datetime import datetime
    x = datetime.now()
    y = "Koha aktuale e paisjes tuaj eshte : " + str(x)
    return y


def LOJA():
    x = random.sample(range(1, 35), 5)
    y = "Numra te cfaredoshem ne rangun [1,35] : " + str(x)
    return y


def GCF(a, b):
    if (b == 0):
        return a
    else:
        return GCF(b, a % b)


def KONVERTO(a, b):
    if a == "CMTOINCH":
        x = 0.0328 * b
        y = "" + str(x) + "inch"
        return y
    elif a == "INCHTOCM":
        x = b / 0.032808
        y = "" + str(x) + "cm"
        return y
    elif a == "KMTOMILE":
        x = b * 0.62137
        y = "" + str(x) + "miles"
        return y
    elif a == "MILETOKM":
        x = b / 0.62137
        y = "" + str(x) + "km"
        return y


def KOHAEMBERRITJES(num):
        num = float(num)
        v = 50000/3600
        t = num / v
        pergjigja = "Per shpejtesi 50 km/h dhe per rrugen " + str(num) + " metra koha e mberritjes eshte " + str(t)+ " sekonda"
        return pergjigja


def SQRT(numri) :
      num = float(numri)
      num_sqrt = num ** 0.5
      pergjigja = "Rrenja katrore: " + str(num_sqrt) 
      return pergjigja

 
while True:
    kerkesa,address=serveri.recvfrom(128)
    kerkesa = kerkesa.upper()
    kerkesa = kerkesa.decode()
    teksti = kerkesa.split(" ")
    print('Kerkesa nga klienti:' + kerkesa)
    if teksti[0] == "IP":
        mesazhi = str(IP(address))
        serveri.sendto(str.encode(mesazhi),address)
    elif teksti[0] == "NRPORTI" :
     mesazhi = str(NRPORTI(address))
     serveri.sendto(mesazhi.encode(),address)
    elif teksti[0] =="NUMERO" :
     mesazhi = str(NUMERO(kerkesa[len(teksti[0]):len(kerkesa)]))
     serveri.sendto(mesazhi.encode(),address)
    elif teksti[0] =="ANASJELLTAS" :
     mesazhi = str(ANASJELLTAS(kerkesa[len(teksti[0]):len(kerkesa)]))
     serveri.sendto(mesazhi.encode(),address)
    elif teksti[0] =="PALINDROME" :
     mesazhi = str(PALINDROME(teksti[1]))
     serveri.sendto(mesazhi.encode(),address)
    elif teksti[0] == "KOHA" :
      mesazhi = str(KOHA())
      serveri.sendto(mesazhi.encode(),address)
    elif teksti[0] == "LOJA" :
      mesazhi = str(LOJA())
      serveri.sendto(mesazhi.encode(),address)
    elif teksti[0] == "GCF" :
      try:
       mesazhi = str(GCF(int(teksti[1]),int(teksti[2])))
      except Exception:
       mesazhi = "Ka ndodhur nje gabim. Ju lutem shkruani metoden gcf dhe dy numra per te realizuar metoden."
      serveri.sendto(mesazhi.encode(),address)

    elif teksti[0] == "KONVERTO" :
      try:
       mesazhi = str(KONVERTO(teksti[1],int(teksti[2])))
      except Exception :
       mesazhi = "Ka ndodhur nje gabim. Ju lutem shkruani metoden cmtofeet/feettocm/milestokm/kmtomiles dhe nje numer te plote."
      serveri.sendto(mesazhi.encode(),address)
  
   
    elif teksti[0]=="KOHAEMBERRITJES":
       try:
        mesazhi=str(KOHAEMBERRITJES(teksti[1]))
       except Exception:
        mesazhi = "ka ndodhur nje gabim ju lutem shkruani funksionin mire"  
       serveri.sendto(mesazhi.encode(),address)
  

    elif teksti[0]=="SQRT":
      try:
       mesazhi=str(SQRT(teksti[1])) 
      except Exception:
       mesazhi="ka ndodhur nje gabim " 
      serveri.sendto(mesazhi.encode(),address)

    elif teksti[0]=="stop" :
      break
    print('Perfundoj komunikimi!')


