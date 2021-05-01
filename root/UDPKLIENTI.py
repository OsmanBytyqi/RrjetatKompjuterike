import socket
import sys
from termcolor import colored
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint

from pyfiglet import figlet_format
from pyfiglet import Figlet
print_red=lambda x:cprint(x,'red')
print_green=lambda x:cprint(x,'green')

from colorama import Fore, Style

inp = input("A deshironi te vazhdoni me vlerat default te serverit? [Y/n] :")#pyesim klinetin nese deshiron te vazhdoj me vlerat default
if inp == "n" :
  EmriServerit = input("Shkruai ipaddressen e re :")
  PortiServerit = int(input("Shkruani portin e ri :"))
else :
  EmriServerit = 'localhost'
  PortiServerit = 14000
try:
     Klienti = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     Klienti.connect((EmriServerit,PortiServerit))
except Exception :
         print_red("Nuk eshte realizuar lidhja mes klientit dhe serverit.")



         print_red("==========================================================")
         print((colored(figlet_format("Try Again"), color="red")))
         print_red("==========================================================")
         
 
else:         

 print_green("===============================================================================")
 print((colored(figlet_format("UDP-KLIENTI!"), color="green")))
 print_green("===============================================================================")
 
 while True:
     print("Per IP shtypni IP")
     print("Per Port shtypni NRPORTI")
     print("Nese deshironi ta dini sa bashtingllore dhe zanore ka nje fjale, shtypeni NUMERO dhe fjalen qe deshironi")
     print("Per te pare kohen shtypni KOHA")
     print("Per te luajtur lojen Keno shtypni LOJA")
     print("Per ta ndryshuar renditjen e nje fjale shkruani ANASJELLTAS dhe fjala qe deshironi")
     print("Per te llogaritur kohen se per sa mberrini deri ne destionation shkruani KOHAEMBERRITJES dhe rrugen ne metra")
     print("Per te pare rrenjen katrore te numrit shtypni SQRT")
     print("Per ta shikuar qe a eshte nje fjala PALINDROME shkruani PALINDROME fjala ")
     print("Per GCF dhe dy numera")
     print("Per konvertimin shkruani KONVERTO CMTOINCH/INCHTOCM/KMTOMILE/MILETOKM")
     print("\nJu lutemi me poshte shkruani kerkesen tuaj!")
     teksti = input("Shkruani kerkesen(nese nuk deshironi te vazhdoni shtypni stop): ")
     if teksti == "stop":
         sys.exit()
     mesazhi = ''
     Klienti.sendto(teksti.encode(),(EmriServerit,PortiServerit))
     TeDhenat,Adresa = Klienti.recvfrom(128)
     mesazhi += TeDhenat.decode("utf-8")
    

     my_str=f"{Style.RESET_ALL}Te dhenat e qe u pranuan nga serveri: {Fore.GREEN} "+ mesazhi 
     print(my_str)
     mystil=f"{Style.RESET_ALL}"
     print(mystil)




     
     print ("-------------------------------------------------------------------------")
 Klienti.close()

 
 