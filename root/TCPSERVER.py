import socket
import random
import datetime
import threading

import sys
from termcolor import colored
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint

from pyfiglet import figlet_format
from pyfiglet import Figlet
print_red=lambda x:cprint(x,'red')
print_green=lambda x:cprint(x,'green')

from datetime import datetime

f=Figlet(font='slant')



def IP(para):
    return para[0]

def NRPORTI(para):
    return para[1]

def NUMERO(para):
    zanoret = 0
    bashketingelloret = 0
    for z in para:#pemes arrayit i kemi deklaruar zanore dhe bashktinglloret
        if z in ['a','e','ë','i','o','u','y','A','E','Ë','I','O','U','Y']:
            zanoret += 1
        elif z in ['b', 'c', 'ç', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z',
                   'B', 'C', 'Ç', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z']:
            bashketingelloret += 1
    x = "Zanore :" +str(zanoret) # i kemi kthyer ne string
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
    x = datetime.now()
    y = "Koha aktuale ne pasijen  tuaj eshte : " + str(x)
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


class Client(threading.Thread):
    def __init__(self,Adresa,Klienti):
        threading.Thread.__init__(self)
        self.ksocket = Klienti
        print ("U shtua komunikimi me klientin i cili ka adresen ", Adresa)
    def run(self):
        while True:
            kerkesa = self.ksocket.recv(128)
            kerkesa = kerkesa.decode()
            kerkesa = kerkesa.upper()
            teksti = kerkesa.split(" ")
            print('Kerkesa nga klienti:' + kerkesa)
            try:
                if teksti[0] == "IP":
                    mesazhi = str(IP(Adresa))
                elif teksti[0] == "NRPORTI":
                    mesazhi = str(NRPORTI(Adresa))
                elif teksti[0] == "NUMERO":
                     mesazhi = str(NUMERO(kerkesa[len(teksti[0]):len(kerkesa)]))
                elif teksti[0] == "ANASJELLTAS":
                    mesazhi = str(ANASJELLTAS(kerkesa[len(teksti[0]):len(kerkesa)]))
                elif teksti[0] == "PALINDROME":
                    mesazhi = str(PALINDROME(teksti[1]))
                elif teksti[0] == "KOHA":
                    mesazhi = str(KOHA())
                elif teksti[0] == "LOJA":
                    mesazhi = str(LOJA())

                elif teksti[0] == "GCF":
                    try:
                     mesazhi = str(GCF(int(teksti[1]), int(teksti[2])))
                    except Exception:
                     mesazhi = "Ka ndodhur nje gabim. Ju lutem shkruani metoden GCF dhe dy numra per te realizuar FUNKSIONIN."
                elif teksti[0] == "KONVERTO": 
                    try:
                     mesazhi = str(KONVERTO(teksti[1], int(teksti[2])))
                    except Exception :
                     mesazhi = "Ka ndodhur nje gabim. Ju lutem shkruani metoden cmtoinch/inchtocm/milestokm/kmtomiles dhe nje numer te plote."
                
                elif teksti[0]=="KOHAEMBERRITJES":
                    try:
                        mesazhi=str(KOHAEMBERRITJES(teksti[1]))
                    except Exception:
                        mesazhi = "ka ndodhur nje gabim ju lutem shkruani funksionin mire"  

                elif teksti[0]=="SQRT":
                    try:
                        mesazhi=str(SQRT(teksti[1])) 
                    except Exception:
                        mesazhi="ka ndodhur nje gabim "             

                elif teksti[0]=="stop" :
                    mesazhi = "Klienti ka nderprere lidhjen me serverin"
                    break
                else:
                    mesazhi = str(dict[teksti[0]()](self.ksocket))
            except Exception:
                mesazhi = "Ka ndodhur nje gabim."
            finally:
                print("Mesazhi i derguar: "+ mesazhi)
                self.ksocket.send(mesazhi.encode())
        print('Perfundoj komunikimi')
     
           
EmriServerit = 'localhost'
PortiServerit = 14000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((EmriServerit, PortiServerit))
print_green("===============================================================================")
print((colored(figlet_format("SERVERI-TCP!"), color="green")))
print_green("===============================================================================")
print("Serveri eshte duke pritur per qdo kerkese te klientit ...")
while True:
    server.listen(5)
    Klienti, Adresa = server.accept()
    newthread = Client(Adresa, Klienti)#kemi deklaruar nje objekt te klases 
    newthread.start()
