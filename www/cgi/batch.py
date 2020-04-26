import cgi, cgitb
import mysql.connector
import json

cgitb.enable()

data = cgi.FieldStorage()
action = data.getValue('action','')

mdb = mysql.connector.connect(host='localhost',user='david',passwd='dw0903',database='dwbrew')
m = mdb.cursor()

if action == 'getList':
    m.execute("SELECT id,name,type,startDate FROM batches")
    resp = m.fetchAll()
    print("Content-Type: text/html")
    print("")
    print(json.dumps(resp))

if action == 'newBatch':
    name = data.getValue('name','batch1')
    type = data.getValue('type','Pale Ale')
    grain = data.getValue('grain','')
    hops = data.getValue('hops','')
    yeast = data.getValue('yeast','')
    mash = data.getValue('mash','17')
    sparge = data.getValue('sparge','14')
    ferment = data.getValue('ferment','23')
    sql = "INSERT INTO batches (name,type,grain,hops,yeast,mashVolume,spargeVolume,fermentVolume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (name,type,grain,hops,yeast,mash,sparge,ferment)
    m.execute(sql,val)
    mdb.commit()
    print("Content-Type: text/html")
    print("")
    print("OK",m.lastrowid)

