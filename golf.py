s={"h":5,"u":5};n=input("Name? ")
while 1:
 print(s);c=input("1 feed 2 play 3 nothing:")
 if c=="1":s["u"]-=2;s["h"]-=1
 elif c=="2":s["h"]+=2;s["u"]+=1
 elif c=="3":s["h"]-=1;s["u"]+=1
 s["u"]+=1;s["h"]-=1
 if s["u"]>9:print(n,"starved");break
 if s["h"]<1:print(n,"left");break
