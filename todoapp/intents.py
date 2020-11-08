item={
    "men":{"Solid Men Polo Neck White, Black T-Shirt":"394","Regular Fit Men Black Polycotton Trousers":"1615","Men Boxy Fit Self Design Spread Collar Formal Shirt":"1259"},
    "furniture":{"Carol Engineered Wood Queen Bed ":"8990","Perfect Homes Cocos sofa":"10,999","Cocos Solid Wood four Seater Dining Set":"9499"},
    "kids":{"Boys Printed Cotton Blend T Shirt":"600","Baby Boys Casual T-shirt Shorts ":"555","Boys Regular Fit Printed Casual Shirt":"595"}
}
orderElement={}
Name=""
zigzag=0

def getIntent(info):
    global Name
    global zigzag
    msg= info['message'].lower()
    if info['key']=='name':
        Name=info["message"]
        return "next"
    elif any(x in msg for x in ["place","order"]):
        zigzag+=1
        if(not checkList(msg)):
            return "notorderd"
        return "ordermsg"
    elif "mens" in msg:
        return "mens"
    elif "furniture" in msg:
        return "furniture"
    elif "kids" in msg:
        return "kids"
    elif "bye" in msg:
        return "bye"
    elif any(x in msg for x in ["available","cash on","on delivery"]):
        return "cod"
    elif any( x in msg for x in ["payment methods","available methods","for payment"]):
        return "paymthds"
    else:
        return "echo"

def handle(data):
    global Name
    global zigzag
    from flask import render_template
    if getIntent(data)=="next":
        return render_template('messages/greet.html',question={'key':'','text':"what do you want to do"},name=Name)
    elif getIntent(data)=="mens":
        return render_template('messages/menswear.html',question={'key':'','text':"Enjoy shopping mens wear"})
    elif getIntent(data)=="furniture":
        return render_template('messages/furnitures.html',question={'key':'','text':"Shop furniture for home"})
    elif getIntent(data)=="kids":
        return render_template('messages/kidswear.html',question={'key':'','text':"Enjoy shopping kids wear"})
    elif getIntent(data)=="ordermsg":
        return render_template("messages/replyfororder.html",question={'key':'','text':"place order"},Zigzag=zigzag,name=Name)
    elif getIntent(data)=="notordered":
        return render_template("messages/notfoud.html",question={'key':'','text':"product not found"})
    elif getIntent(data)=="getmyorders":
        return render_template("messages/getorders.html",question={'key':'','text':"getting products"})
    elif getIntent(data)=="cod":
        return render_template("messages/codmain.html",question={'key':'','text':"getting products"},name=Name)
    elif getIntent(data)=="paymthds":
        return render_template("messages/paymain.html",question={'key':'','text':"getting products"})
    elif getIntent(data)=="bye":
        return render_template("messages/bye.html",name=Name)
    else:
        return render_template('messages/nreq.html',question=data)


presentItem=[]
trackOrder={}
com=["i","place","order","for","want","buy"]

def checkList(info):
    global trackOrder
    maxMatch=0
    countmatch=0
    iteValue=0
    iteElement=""
    gotItem=set(info.split())

    gotItem=set(info.split())
    gotItems=[x for x in gotItem if x not in com]

    for cat in item:
        for key,val in item[cat].items():
            countmatch=0
            key=key.lower()

            presentItem=set(key.split())

            res=(set(gotItems)).intersection(presentItem)
            countmatch=len(res)
            if maxMatch<countmatch:
                
                iteElement=key
                iteValue=val
                maxMatch=countmatch
       
                return True

    return False
    
checkList(" i want to shop boxy fit mens")



            