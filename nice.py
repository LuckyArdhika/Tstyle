#Open the index
# - *- coding: utf- 8 - *-
#CreatedCyXNot404
#recode ga bakal bikin lu pro!

blue='\033[94m'
green='\033[92m'
purple='\033[95m'
cyan='\033[96m'
red='\033[91m'
white='\033[97m'
yellow='\033[93m'

god = """======================================================================="""

mes = """          +=============================================+
          |		P3M3R24NT1Q 73RMUX		|
	  +---------------------------------------------+
	  |		Created By CyXNot404		|
	  |         Instagram     : chg.official        |
          |         Whatsapp      : 081578857166	|
          |          facebook.com/lucky.ardhika         |
	  |         Youtube       : LuckyArd110         |
          +---------------------------------------------+
	  |   •   •   Dark Xploit Cyber Team   •   •    |
          +=============================================+
v2py2#~ """

import os
import sys
import time
import random
import cookielib
import mechanize

os.system('clear')

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
print
mengetik("\033[96mLOADING...") 
time.sleep(0.5)
os.system('clear')
print mes
print
print god
print
print "\033[92mPilihAn Tersedia:"
print "Opsional Gaya Termux:"
print
print "\033[92m[1] Eyes                              [9] Neofetch"
print "[2] Teks Nama (figlet slant)          [10] Screenfetch"
print "[3] Eyes + Teks Nama (figlet slant)   [11] Teks Nama Blok"
print "[4] Dragon                            [12] Anonymous Logo"
print "[5] TERmux cowsay                     [13] Data Diri"
print "[6] Ghostbusters                      [14] cmatrix effect"
print "[7] Eyes + gay font                   [15] Teks Nama (gay)"
print "[8] Turkey""                            \033[91m[16] 1N$T4L 84H4N" 
print
print god

p = raw_input("\033[93mMasukkan Pilihan : ")
print "\033[96m "
print god

if p == '1':
    os.system('cowsay -f eyes "Nama/Teks" | lolcat')
    name = str(raw_input(' [?]\033[96m Masukkan Nama/teks :\033[92m '))
    mengetik('proccess..')
    mengetik('\033[96m<||||||||||||||||||||||||||||||||||||||||||||||||]>')
    time.sleep(1)
    print god
    fo = open('bash.bashrc','w')
    fo.write('clear')
    fo.write('\ncowsay -f eyes "'+name)
    fo.write('" | lolcat\n')
    fo.write("date | lolcat\n")
    fo.write("PS1='\033[92m╭────•root@CyXNot404#")
    fo.write("\n╰──• '")
    fo.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    print "           \033[92mProses Selesai...!"
    print "           \033[97mLogin Ulang Termux Dalam 3 detik"
    time.sleep(3)
    os.system('login')

if p == '2':
    os.system('figlet -f slant "SlantStyle" | lolcat')
    name = str(raw_input(' [?]\033[96m Masukkan Teks Figlet :\033[92m '))
    mengetik('proccess..')
    mengetik('\033[96m<||||||||||||||||||||||||||||||||||||||||||||||||]>')
    time.sleep(1)
    print god
    fo = open('bash.bashrc','w')
    fo.write('clear')
    fo.write('\nfiglet -f slant "'+name)
    fo.write('" | lolcat\n')
    fo.write("date | lolcat\n")
    fo.write("PS1='\033[92m╭────•root@CyXNot404#")
    fo.write("\n╰──• '")
    fo.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    print "           \033[92mProses Selesai...!"
    print "           \033[97mLogin Ulang Termux Dalam 3 detik"
    time.sleep(3)
    os.system('login')

if p == '3':
    os.system('cowsay -f eyes "Nama/Teks" | lolcat')
    os.system('figlet -f slant "TeksFiglet" | lolcat')
    name = str(raw_input(' [?]\033[96m Masukkan Nama/teks :\033[92m '))
    usr = str(raw_input(' [?]\033[96m Masukkan Teks Figlet :\033[92m'))
    mengetik('proccess..')
    mengetik('\033[96m<||||||||||||||||||||||||||||||||||||||||||||||||]>')
    time.sleep(1)
    print god
    fo = open('bash.bashrc','w')
    fo.write('clear')
    fo.write('\ncowsay -f eyes "'+name)
    fo.write('" | lolcat\n')
    fo.write('figlet -f slant "'+usr)
    fo.write('" | lolcat\n')
    fo.write("date | lolcat\n")
    fo.write("PS1='\033[92m╭────•root@CyXNot404#")
    fo.write("\n╰──• '")
    fo.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    print "           \033[92mProses Selesai...!"
    print "           \033[97mLogin Ulang Termux Dalam 3 detik"
    time.sleep(3)
    os.system('login')

if p == '4':
   os.system('cowsay -f dragon "Teks/Nama" | lolcat')
   print god
   name = str(raw_input(' [?]\033[96m Masukkan Nama/teks :\033[92m '))
   mengetik('\033[96m<||||||||||||||||||||||||||||||||||||||||||||||||]>')
   time.sleep(1)
   print god
   fo = open('bash.bashrc','w')
   fo.write('clear\n')
   fo.write('cowsay -f dragon "'+name)
   fo.write('" | lolcat\n')
   fo.write('date | lolcat\n')
   fo.write("PS1='\033[92m╭────•root@CyXNot404#")
   fo.write("\n╰──• '")
   fo.close()
   os.system("rm $HOME/../usr/etc/bash.bashrc")
   os.system("cp -f bash.bashrc $HOME/../usr/etc")
   print "           \033[92mProses Selesai...!"
   print "           \033[97mLogin Ulang Termux Dalam 3 detik"
   time.sleep(3)
   os.system('login')

if p == '5':
   os.system('cowsay -f termux "Teks/Nama" | lolcat')
   print god
   name = str(raw_input(' [?]\033[96m Masukkan Nama/teks :\033[92m '))
   mengetik('\033[96m<||||||||||||||||||||||||||||||||||||||||||||||||]>')
   time.sleep(1)               
   print god
   fo = open('bash.bashrc','w')                                                              
   fo.write('clear\n')
   fo.write('cowsay -f termux  "'+name)                                                       
   fo.write('" | lolcat\n')
   fo.write('date | lolcat\n')
   fo.write("PS1='\033[92m╭────•root@CyXNot404#")
   fo.write("\n╰──• '")
   fo.close()
   os.system("rm $HOME/../usr/etc/bash.bashrc")
   os.system("cp -f bash.bashrc $HOME/../usr/etc")
   print "           \033[92mProses Selesai...!"
   print "           \033[97mLogin Ulang Termux Dalam 3 detik"
   time.sleep(3)
   os.system('login')

if p == '6':
   os.system('cowsay -f ghostbusters "Teks/Nama" | lolcat')
   print god
   name = str(raw_input(' [?]\033[96m Masukkan Nama/teks :\033[92m '))
   mengetik('\033[96m<||||||||||||||||||||||||||||||||||||||||||||||||]>')
   time.sleep(1)
   print god
   fo = open('bash.bashrc','w')
   fo.write('clear\n')
   fo.write('cowsay -f ghostbusters  "'+name)
   fo.write('" | lolcat\n')
   fo.write('date | lolcat\n')
   fo.write("PS1='\033[92m╭────•root@CyXNot404#")
   fo.write("\n╰──• '")
   fo.close()
   os.system("rm $HOME/../usr/etc/bash.bashrc")
   os.system("cp -f bash.bashrc $HOME/../usr/etc")
   print "           \033[92mProses Selesai...!"
   print "           \033[97mLogin Ulang Termux Dalam 3 detik"
   time.sleep(3)
   os.system('login')

if p == '7':
   os.system('cowsay -f eyes "Nama/Teks" | lolcat')
   os.system('toilet -f standard "Teks Gay" -F gay ')
   name = str(raw_input(' [?]\033[96m Masukkan Nama/teks :\033[92m '))
   usr = str(raw_input(' [?]\033[96m Masukkan Teks Gay :\033[92m '))
   mengetik('proccess..')
   mengetik('\033[96m<||||||||||||||||||||||||||||||||||||||||||||||||]>')
   time.sleep(1)    
   print god
   fo = open('bash.bashrc','w')
   fo.write('clear')
   fo.write('\ncowsay -f eyes "'+name)
   fo.write('" | lolcat\n')
   fo.write('toilet -f standard "'+usr)
   fo.write('" -F gay\n')
   fo.write("date | lolcat\n")
   fo.write("PS1='\033[92m╭────•root@CyXNot404#")
   fo.write("\n╰──• '")
   fo.close()
   os.system("rm $HOME/../usr/etc/bash.bashrc")
   os.system("cp -f bash.bashrc $HOME/../usr/etc")
   print "           \033[92mProses Selesai...!"
   print "           \033[97mLogin Ulang Termux Dalam 3 detik"
   time.sleep(3)
   os.system('login')

if p == '8':
   os.system('cowsay -f turkey "Teks/Nama" | lolcat')
   print god
   name = str(raw_input(' [?]\033[96m Masukkan Nama/teks :\033[92m '))
   mengetik('\033[96m<||||||||||||||||||||||||||||||||||||||||||||||||]>')
   time.sleep(1)
   print god
   fo = open('bash.bashrc','w')
   fo.write('clear\n')
   fo.write('cowsay -f turkey  "'+name)
   fo.write('" | lolcat\n')
   fo.write('date | lolcat\n')
   fo.write("PS1='\033[92m╭────•root@CyXNot404#")
   fo.write("\n╰──• '")
   fo.close()
   os.system("rm $HOME/../usr/etc/bash.bashrc")
   os.system("cp -f bash.bashrc $HOME/../usr/etc")
   print "           \033[92mProses Selesai...!"
   print "           \033[97mLogin Ulang Termux Dalam 3 detik"
   time.sleep(3)
   os.system('login')

if p == '9':
   os.system('neofetch | lolcat')
   print god
   pgr = str(raw_input(' [?]\033[96m Masukkan Nama user :\033[92m '))
   mengetik('\033[96m<||||||||||||||||||||||||||||||||||||||||||||||||]>')
   time.sleep(1)
   print god
   fo = open('bash.bashrc','w')
   fo.write('clear\n')
   fo.write('neofetch | lolcat\n')
   fo.write('                   user : ' +pgr)
   fo.write('" | lolcat\n')
   fo.write('date | lolcat\n')
   fo.write("PS1='\033[92m╭────•root@CyXNot404#")
   fo.write("\n╰──• '")
   fo.close()
   os.system("rm $HOME/../usr/etc/bash.bashrc")
   os.system("cp -f bash.bashrc $HOME/../usr/etc")
   print "           \033[92mProses Selesai...!"
   print "           \033[97mLogin Ulang Termux Dalam 3 detik"
   time.sleep(3)
   os.system('login')

if p == '10':
   os.system('screenfetch | lolcat')
   print god
   pgr = str(raw_input(' [?]\033[96m Masukkan Nama user :\033[92m '))
   mengetik('\033[96m<||||||||||||||||||||||||||||||||||||||||||||||||]>')
   time.sleep(1)
   print god
   fo = open('bash.bashrc','w')
   fo.write('clear\n')
   fo.write('screenfetch | lolcat\n')
   fo.write('                   user : ' +pgr)
   fo.write('" | lolcat\n')
   fo.write('date | lolcat\n')
   fo.write("PS1='\033[92m╭────•root@CyXNot404#")
   fo.write("\n╰──• '")                                                                 
   fo.close()
   os.system("rm $HOME/../usr/etc/bash.bashrc")
   os.system("cp -f bash.bashrc $HOME/../usr/etc")
   print "           \033[92mProses Selesai...!"
   print "           \033[97mLogin Ulang Termux Dalam 3 detik"                               
   time.sleep(3)
   os.system('login')

if p == '11':
    os.system('figlet -f block "Teks Block" | lolcat')
    name = str(raw_input(' [?]\033[96m Masukkan Teks Block :\033[92m '))
    mengetik('proccess..')
    mengetik('\033[96m<||||||||||||||||||||||||||||||||||||||||||||||||]>')
    time.sleep(1)
    print god
    fo = open('bash.bashrc','w')
    fo.write('clear')
    fo.write('\nfiglet -f block "'+name)
    fo.write('" | lolcat\n')
    fo.write("date | lolcat\n")
    fo.write("PS1='\033[92m╭────•root@CyXNot404#")
    fo.write("\n╰──• '")
    fo.close()
    os.system("rm $HOME/../usr/etc/bash.bashrc")
    os.system("cp -f bash.bashrc $HOME/../usr/etc")
    print "           \033[92mProses Selesai...!"
    print "           \033[97mLogin Ulang Termux Dalam 3 detik"
    time.sleep(3)
    os.system('login')

if p == '12':
   os.system('cowsay -f anon2 "Teks/Nama" | lolcat')
   print god
   name = str(raw_input(' [?]\033[96m Masukkan Nama/teks :\033[92m '))
   mengetik('\033[96m<||||||||||||||||||||||||||||||||||||||||||||||||]>')
   time.sleep(1)
   print god
   fo = open('bash.bashrc','w')
   fo.write('clear\n')
   fo.write('cowsay -f anon2  "'+name)
   fo.write('" | lolcat\n')
   fo.write('date | lolcat\n')
   fo.write("PS1='\033[92m╭────•root@CyXNot404#")
   fo.write("\n╰──• '")
   os.system("rm $HOME/../usr/etc/bash.bashrc")
   os.system("cp -f bash.bashrc $HOME/../usr/etc")
   print "           \033[92mProses Selesai...!"                                             
   print "           \033[97mLogin Ulang Termux Dalam 3 detik"
   time.sleep(3)
   os.system('login')

if p == '13':
   print god
   print "Di Tunggu Next Update Ya!"
   print god

if p == '14':
   print "Tekan CTRL + Z untuk berhenti"
   p = raw_input('ENTER jika mengerti!')
   mengetik('Loaded..............')
   time.sleep(1)
   os.system('cmatrix')

if p == '15':
   os.system('toilet -f standard "Teks Gay" -F gay ')
   print god
   usr = str(raw_input(' [?]\033[96m Masukkan Teks Gay :\033[92m '))
   mengetik('proccess..')
   mengetik('\033[96m<||||||||||||||||||||||||||||||||||||||||||||||||]>')
   time.sleep(1)
   print god
   fo = open('bash.bashrc','w')
   fo.write('clear\n')
   fo.write('toilet -f standard "'+usr)                                                                  
   fo.write('" -F gay\n')
   fo.write("date | lolcat\n")
   fo.write("PS1='\033[92m╭────•root@CyXNot404#")
   fo.write("\n╰──• '")                                                                                  
   fo.close()
   os.system("rm $HOME/../usr/etc/bash.bashrc")                                                          
   os.system("cp -f bash.bashrc $HOME/../usr/etc")
   print "           \033[92mProses Selesai...!"
   print "           \033[97mLogin Ulang Termux Dalam 3 detik"
   time.sleep(3)                                                                                         
   os.system('login')

if p == '16':
   os.system('pkg install nano')
   os.system('pkg install cmatrix')
   os.system('pkg install cowsay')
   os.system('pkg install figlet')   
   os.system('pkg install neofetch')
   os.system('pkg install screenfetch')
   os.system('pkg install lolcat')
   os.system('cd')
   os.system('git clone https://github.com/LuckyArd110/Termuxc')
   os.system('cd Termuxc')
   os.system('mv termux.cow /../usr/share/cows')
   os.system('mv anon2.cow /../usr/share/cows')
   mengetik('\033[96m<||||||||||||||||||||||||||||||||||||||||||||||||||||||||||]>100%')
   print god
   print "         \033[96mProses Selesai! Otomatis Ke menu utama"
   time.sleep(2)
   os.system('python2 project.py')
