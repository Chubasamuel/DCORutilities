import xlrd as x
from datetime import datetime as dt
import json

cyan = "\33[96m"
bold = "\33[1m"
red = "\33[91m"
green = "\33[32m"
cend = "\033[m"

base_path = "../../../../Documents/exp"
book=x.open_workbook(base_path+"/expenses.xls")
sh=book.sheet_by_index(0)
em={}

config = {}
with open(base_path+"/config.json", "r") as f:
    config = json.load(f)


indexes={"date":0,"purpose":1,"income":2,"expense":3,"category":4,"description":5}

def invCategOrPurp(categOrPurpM,isCateg,inc, dd,mm,yy,dd2,mm2,yy2):
    ccCategP = categOrPurpM.split(":")
    categOrPurp = ccCategP[0]
    shouldMergeKey=False
    if(len(ccCategP)>1 and ccCategP[1].strip()=="m"):
        shouldMergeKey=True
    
    res = {"c_o_u_n_t":{}}
    incOrExp=2
    catOrP=1
    if isCateg:
        catOrP=indexes["category"]
    else:
        catOrP=indexes["purpose"]
    if inc:
        incOrExp=indexes["income"]
    else:
        incOrExp=indexes["expense"]
    for r in range(sh.nrows):
        dddd=sh.cell_value(rowx=r,colx=indexes["date"])
        try:
            cD,cM,cY=[int(i) for i in str(dddd).split("-")]
        except:
            continue
        if withinDate(cD,cM,cY,dd,mm,yy,dd2,mm2,yy2):
            v=sh.cell_value(rowx=r,colx=catOrP)
            cV=sh.cell_value(rowx=r,colx=incOrExp)
            if categOrPurp.lower()==v.lower():
                if cV=="" or str(cV).strip()=="":
                    continue
                putOrUp(res,categOrPurp,cV)
            elif categOrPurp.lower() in v.lower():
                if cV=="" or str(cV).strip()=="":
                    continue
                if(shouldMergeKey):
                    putOrUp(res,categOrPurp,cV)
                else:
                    putOrUp(res,v,cV)
    return res


def putOrUp(dic,key,val):
    if key in dic:
        dic[key]+=val
        dic["c_o_u_n_t"][key]+=1
    else:
        dic[key]=val
        dic["c_o_u_n_t"][key]=1

def withinDate(cD,cM,cY,dd,mm,yy,dd2,mm2,yy2):
    t=dt(cY,cM,cD).timestamp()
    t1=dt(yy,mm,dd).timestamp()
    t2=dt(yy2,mm2,dd2).timestamp()
    return t>=t1 and t<=t2
def printL(res):
    for k in res:
        if(k=="c_o_u_n_t"):
            print("{'c_o_u_n_t': ",res["c_o_u_n_t"],sep="", end="")
        else:
            print(", '",k,"': ",green,res[k],cend,"}", sep="")
for c in config:
    d,m,y=[int(i) for i in c["start"].split("-")]
    d2,m2,y2=[int(i) for i in c["end"].split("-")]
    params = c["params"].split(",")
    isCateg = c["isCateg"]
    isInc = c["isInc"]
    res = [invCategOrPurp(i.strip(),isCateg,isInc, d,m,y,d2,m2,y2) for i in params]
    print(bold,green,"from: ",cend,c["start"])
    print(bold,green,"to: ",cend, c["end"])
    for r in res:
        print(cyan,bold,"-- ",cend,end="")
        print(bold,end="",)
        printL(r)
        print(cend)
    print("\n\n")

