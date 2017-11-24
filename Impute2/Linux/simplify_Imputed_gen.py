#!/usr/bin/python3
import sys
MyfileName=sys.argv[1]

#in Python3 :
myFile=open(MyfileName,"r")
resName=MyfileName + ".simple.txt"
result=open(resName,"w")
lines=myFile.readlines()
for li in lines :
    li=li.split(" ")
    l=" ".join (li[0:5])
    for i in range(163) :
        a=li[5+3*i]
        b=li[6+3*i]
        c=li[7+3*i]
        if float(a)>=0.9 :
          l = l + " 0"
        elif float(b) >= 0.9 :
          l = l + " 1"
        elif float(c)>=0.9 :
          l = l + " 2" 
        else :
          l = l + " " + str(max(float(a),float(b),float(c)))
    l=l+"\n"
    result.write(l)

result.close()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Old one in bash:
#~ for ligne in $(cat Imputed_R2.gen); do
    #~ echo -n "."
    #~ l=$(echo $ligne | cut -f 1-5 -d " ")
    #~ for i in $(seq 6 3 492); do 
      #~ a=$(echo $ligne | cut -f $i -d " "); 
      #~ b=$(echo $ligne | cut -f `expr $i + 1` -d " "); 
      #~ c=$(echo $ligne | cut -f `expr $i + 2` -d " ");
      #~ if (( $(echo "$a >= 0.9" | bc -l) )); then l="${l} 0"; 
      #~ elif (( $(echo "$b >= 0.9" | bc -l) )); then l="${l} 1";
      #~ elif (( $(echo "$c >= 0.9" | bc -l) )); then l="${l} 2"; 
      #~ else 
        #~ l="$l $(echo -e "$a\n$b\n$c" | sort -nr | head -n1)"
      #~ fi
    #~ done
    #~ echo $l >> Imputed_R2_simple.txt
#~ done
