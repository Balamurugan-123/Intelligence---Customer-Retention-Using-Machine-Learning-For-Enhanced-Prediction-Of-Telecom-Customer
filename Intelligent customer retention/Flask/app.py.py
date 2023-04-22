from flask import Flask, render_template, request
import keras
from tensorflow.python.keras.models import load_model
app = Flask(__name__)
model = load_model("telecom_churn.h5")
@app.route('/')
def home():
    return render_template('home.html')
    @app.route('/')
    def helloworld():
        return render_template("base.html")
    app.route('\predict',methods=['post'])
    def admin():
        a=request.form["gender"]
        if(a=='f'):
            a=0
        if(a=='m'):
            a=1
        b=request.form["srcitizen"] 
        if(b=='n'):
            b=0
        if(b=='y'):
            b=1
        c=request.form["partner"]
        if(c=='n'):
            c==0
        if(c=='y'):
            c=1
        d=request.form["departments"]
        if(d=='n'):
           d=0
        if(d=='y'):
            d=1
        e=request.form["tenure"] 
        f=request.form["phservices"]
        if(f=='n'):
            f=o
        if(f=='y'):
            f=1
        g=request.form["multi"] 
        if (g== 'n'):
            l1,l2,l3=1,0,0
        if (1 == 'nis'):
            l1,l2,l3=0,1,0
        if (l == 'y'):
            l1,l2,l3=0,0,1
        m=request.form["stv"]
        if (m == 'n'): 
            m1,m2,m3=1,0,0
        if (m == 'nis'):
            m1,m2,m3=0,1,0
        if (m == 'y'):
            m1,m2,m3=0,0,1
        n= request.form["smv"]
        if (n == 'n'):
            n1,n2,n3=1,0,0
        if (n == 'nis'):
            n1,n2,n3=0,1,0
        if (n == 'y'):
            n1,n2,n3=0,0,1
        o= request.form["contract"] 
        if (o == 'mtm'):
            o1,o2,o3=1,0,0
        if (o =='oyr'):
            o1,o2,o3=0,1,0
        if (0 == 'tyrs'):
            o1,o2,o3=0,0,1
        p= request.form["pmt"]
        if (p == 'ec'):
            p1,p2,p3,p4=1,0,0,0
        if (p == 'mail'):
            p1,p2,p3,p4=0,1,0,0
        if (p == 'bt'):
            p1,p2,p3,p4=0,0,1,0
        if (p == 'c'):
            p1,p2,p3,p4=0,0,0,1
        q= request.form["plb"]
        if (q == 'n'):
            q=0
        if (q == 'y'):
            q=1
        r= request.form["mcharges"]
        s= request.form["tcharges"]

        t=[[int(g1),int(gg2),int(g3),int(h1),int(h2),int(h3),int(i1),int(i2),int(i3),int(j1),int(j2),int(j3)]]
        print(t)
        x = model.predict(t)
        print(x[0])
        if (x[[0]] <=0.5):
            y ="No"
            return render_template("predno.html", z = y)
        
        if (x[[0]] >= 0.5):
            y ="Yes"
            return render_template("predyes.html", z = y)