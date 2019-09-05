"""
Yes! I Jeremiah Chuba Samuel wrote this script to help me track my quizzes scores, !nd also for some of my friends and I care about.

"""
import sys
import ast
import base64
import re

mode="";
comList=["aqn","dump"];
ccyan="\33[96m";
cbold="\33[1m";
cred="\33[91m";
cgreen="\33[32m";
cend="\033[m";

def err(a):
    print("\33[91m\33[1m",a.title(),"\033[m")
def succ(a):
    print("\33[32m\33[1m",a.title(),"\033[m")

try:
    open("rec.dt","rb").read();
except (FileNotFoundError,OSError) as e:
    err("Notice:: The data storage file was not found or there was permission issues, a new one will be created.  Don't worry! This only happens when you are running this program for the first time");
    try:
        open("rec.dt","wb+").write(base64.b64encode(bytes("{}","utf-8")));
        succ("Data storage file created successfully");
    except:
        err("Error while trying to create data storage file. May be some file permission issues! So check your settings");
        sys.exit();
with open("rec.dt","rb") as f:
    recordRead=base64.b64decode(f.read()).decode("utf-8","ignore");
    recData=ast.literal_eval(recordRead);
def pMark(a):
    if(float(a)>=50):
        return cgreen+str(a)+cend;
    elif(float(a)<50):
        return cred+str(a)+cend;
    else:
        return a;
def dumpAll():
    sep=2;
    k=recData;
    for i in k:
        for b in k[i]:
            sep=len(b+" "+" ---- "+k[i][b])+3;
        print(ccyan+cbold+i.capitalize()+cend);
        print("-"*sep);
        for a in k[i]:
            print(a.capitalize()," ---- ",pMark(k[i][a]));
        print("-"*sep,"\n");

def dumpN(name):
    k=recData;
    print("\n\n");
    sep=2;

    for b in k[name]:
        sep=len(b+" "+" ---- "+k[name][b])+3;
    print(ccyan+cbold+name.capitalize()+cend);
    print("-"*sep);
    for a in k[name]:
        print(a.capitalize()," ---- ",pMark(k[name][a]));
    print("-"*sep,"\n");

def dumpManyQ(nothing,*args):
    k=recData;
    sep=2;
    print("\n\n\n")
    for i in k:
        tm=[o for o in k[i] if o in args[0]];
        for b in tm:
            sep=len(b+" "+" ---- "+str(k[i][b]))+3;
        print(ccyan+cbold+i.capitalize()+cend);
        print("-"*sep);
        for r in tm:
            if(r in k[i]):
                print(r.capitalize()," ---- ",pMark(k[i][r]));
        print("-"*sep);

def dumpManyN(aq,ar):
    ty=aq.split(",");
    tz=ar.split(",");
    k=recData;
    sep=2;
    print("\n\n\n");
    N=[y for y in k if y in ty];
    for i in N:
        tm=[o for o in k[i] if o in tz];
        for b in tm:
            sep=len(b+" "+" ---- "+str(k[i][b]))+3;
        print(ccyan+cbold+i.capitalize()+cend);
        print("-"*sep);
        for r in tm:
            if(r in k[i]):
                print(r.capitalize()," ---- ",pMark(k[i][r]));
        print("-"*sep);

def dumpQ(quiz):
    k=recData;
    print("\n\n");
    sep=2;
    for i in k:
        for b in k[i]:
            if(quiz in k[i]):
                sep=len(b+" "+" ---- "+str(k[i][quiz]))+3;
        print(ccyan+cbold+i.capitalize()+cend);
        print("-"*sep);
        for nb in k[i]:
            if(quiz in k[i]):
                if(quiz==nb):
                    print(quiz.capitalize()," ---- ",pMark(k[i][quiz]));
        print("-"*sep,"\n");
def pMode():
    global mode 
    mode=input("Enter mode of operation,\"\33[96m \33[1m dump \033[m\" to view previously saved data, \"\33[96m \33[1m aqn \033[m\" to add new data\nOr  Enter \"\33[91m exit \033[m\" to exit program\n\n").lower();
    if mode=='exit':
        print("Program exited")
        sys.exit();
    if(not mode in comList):
        err("\n Command not recognised\n Enter a valid command\n")
        pMode();
    else:
       # print("command exists")
       """"""
pMode();

def aqnInp():
    aqnData=input("Enter new data in format \"\33[96m name:title:value \033[m\" e.g chuba:pharmac1:65\n\n").lower();
    if(aqnData=="exit"):
        err("Program exited");
        sys.exit();
    aqnData=aqnData.split(":");
    with open("rec.dt","rb") as f:
        recRead=base64.b64decode(f.read()).decode("utf-8","ignore");
        rec=ast.literal_eval(recRead);
        if aqnData[0] in rec:
            if not aqnData[1] in rec[aqnData[0]]:
                rec[aqnData[0]][aqnData[1]]=aqnData[2];
            else:
                err("Data "+str(aqnData[1])+" for "+str(aqnData[0]).capitalize()+" already exists\n New entry not saved.");
                sys.exit();
        else:
            rec[aqnData[0]]={};
            rec[aqnData[0]][aqnData[1]]=aqnData[2]
        f.close();
        f=open("rec.dt","wb");
        f.write(base64.b64encode(bytes(str(rec),"utf-8"))); 
        f.close();
        succ("Data added successfully");
        aqnInp();


def dumpFunc():
    dMode=input("\nEnter dump arg e.g formats below::\n\ntitle\nname\nall\nname#title\nname#title,title,title\nname,name#title,title,title,title\nname,name,name,name#title\n OR \" "+cred+"exit"+cend+"\" to exit\n\n" ).lower();
    if(dMode=="exit"):
        err("Program exited");
        sys.exit();

    if(dMode=="all"):
        dumpAll();
        succ("Full data dumped");
        dumpFunc();
    
    elif(dMode.split("#")[0].split(",")[0] in recData and re.search(r"^[\,a-z]+#[\,a-z0-9]+$",dMode)):
        yy=dMode.split("#");
        dumpManyN(yy[0],yy[1]);
        succ("Data for "+dMode+" dumped");
        dumpFunc();
    elif(dMode in recData):
        dumpN(dMode);
        succ("Data for "+dMode+" dumped");
        dumpFunc();
    elif(re.search(",",dMode)):
        yy=dMode.split(",");
        dumpManyQ(0,yy);
        succ("Data for "+dMode+" dumped");
        dumpFunc();
    elif((not dMode in recData)and(re.search("\\b"+dMode+"\\b",str(recData)))):
        dumpQ(dMode);
        succ("Data for "+dMode+" dumped");
        dumpFunc();
    else:
        err("\nDump arg not recognised or data that matches arg was not found");
        dumpFunc();


holder="";
progRun=False;

with open('rec.dt','r+') as f:
    holde=f.read();
    if len(holde)>1:
        holder=ast.literal_eval(base64.b64decode(holde).decode("utf-8","ignore"));
    else:
        holder="";
    if ((type(holder)==dict) or len(holder)<1):
        progRun=True;
       # print("Valid data");
    elif (type(holder)!=dict and len(holder)>1): 
        progRun=False;
        err("Saved data not a valid dict!\nProgram exited");
        f.close();
        sys.exit();
    f.close();
if(mode=="dump"):
    dumpFunc();
elif(mode=="aqn" and progRun==True):
    aqnInp();
else:
    err("Operation failed!");
