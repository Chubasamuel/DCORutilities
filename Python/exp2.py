import xlrd as x
from datetime import datetime as dt

book=x.open_workbook("./expenses.xls")

sh=book.sheet_by_index(0)
em={}
fromDate = input("Enter start date in format dd-mm-yyyy\n\t")
toDate = input("Enter end date in format dd-mm-yyyy\n\t")

indexes={"date":0,"purpose":1,"income":2,"expense":3,"category":4,"description":5}

d,m,y=[int(i) for i in fromDate.split("-")]
d2,m2,y2=[int(i) for i in toDate.split("-")]

def invCategOrPurp(categOrPurp,isCateg,inc):
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
        if withinDate(cD,cM,cY):
            v=sh.cell_value(rowx=r,colx=catOrP)
            cV=sh.cell_value(rowx=r,colx=incOrExp)
            if categOrPurp.lower()==v.lower():
                if cV=="" or str(cV).strip()=="":
                    continue
                putOrUp(res,categOrPurp,cV)
            elif categOrPurp.lower() in v.lower():
                if cV=="" or str(cV).strip()=="":
                    continue
                putOrUp(res,v,cV)
    return res


def putOrUp(dic,key,val):
    if key in dic:
        dic[key]+=val
    else:
        dic[key]=val
def withinDate(dd,mm,yyyy):
    t=dt(yyyy,mm,dd).timestamp()
    t1=dt(y,m,d).timestamp()
    t2=dt(y2,m2,d2).timestamp()
    return t>=t1 and t<=t2

isCateg=True
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
catOrP=catOrP.split(",")

"""inv=["airtime","data","water"]
for i in inv:
    print(invCategOrPurp(i,isCateg,isInc))
"""

"""inv = ["feed","food"]
for i in inv:
    print(invCategOrPurp(i,isCateg,isInc))"""

for c in catOrP:
    print(invCategOrPurp(c.strip(),isCateg,isInc))
