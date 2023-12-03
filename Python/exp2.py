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


#fromDate = input("Enter start date in format dd-mm-yyyy\n\t")
#toDate = input("Enter end date in format dd-mm-yyyy\n\t")

indexes={"date":0,"purpose":1,"income":2,"expense":3,"category":4,"description":5}

def invCategOrPurp(categOrPurpM,isCateg,inc, dd,mm,yy,dd2,mm2,yy2):
    ccCategP = categOrPurpM.split(":")
    categOrPurp = ccCategP[0]
    shouldMergeKey=False
    if(len(ccCategP)>1 and ccCategP[1].strip()=="m"):
        shouldMergeKey=True
    
    res = {}
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
    else:
        dic[key]=val
def withinDate(cD,cM,cY,dd,mm,yy,dd2,mm2,yy2):
    t=dt(cY,cM,cD).timestamp()
    t1=dt(yy,mm,dd).timestamp()
    t2=dt(yy2,mm2,dd2).timestamp()
    return t>=t1 and t<=t2
for c in config:
    d,m,y=[int(i) for i in c["start"].split("-")]
    d2,m2,y2=[int(i) for i in c["end"].split("-")]
    params = c["params"].split(",")
    isCateg = c["isCateg"]
    isInc = c["isInc"]
    res = [invCategOrPurp(i.strip(),isCateg,isInc, d,m,y,d2,m2,y2) for i in params]
    print(bold,green,"from: ",cend,c["start"])
    print(bold,green,"to: ",cend, c["end"])
    print(bold,res,cend)
    print("\n\n")

"""isCateg=True
isInc=False
while True:
    inp=input("Is it a category? (Y/N)\t")
    if inp.lower() =="y":
        isCateg=True
        break
    elif inp.lower()=="n":
        isCateg=False
        break
    else:
        continue
while True:
    inp=input("Is it an income? (Y/N)\t")
    if inp.lower() =="y":
        isInc=True
        break
    elif inp.lower()=="n":
        isInc=False
        break
    else:
        continue
catOrP=input("Enter names of category or purpose separated by comma:\n\t")
catOrP=catOrP.split(",")"""

"""inv=["airtime","data","water"]
for i in inv:
    print(invCategOrPurp(i,isCateg,isInc))
"""

"""inv = ["feed","food"]
for i in inv:
    print(invCategOrPurp(i,isCateg,isInc))"""

"""for c in catOrP:
    print(invCategOrPurp(c.strip(),isCateg,isInc))"""
