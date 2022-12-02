from flask import Flask, render_template, request

import cx_Oracle

connection = cx_Oracle.connect('vxd9845', 'Ashoksai1997', 'acaddbprod.uta.edu:1523/pcse1p.data.uta.edu')

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route("/display", methods = ['get', 'post'])
def display():
  # insert  pass
  if request.method == 'POST':
    relation_nos = list(request.form.values())

    if relation_nos[0] == "relation1":
      cur = connection.cursor()

      cols = cur.execute("select COLUMN_NAME from user_tab_columns where TABLE_NAME='FALL22_S004_14_PAYMENTS'")

      columns = []

      for col in cols:
          print("--col", col)
          columns.append(col[0])
      
      columns = tuple(columns)
      rows_display = []
      rows = cur.execute("select * from Fall22_S004_14_Payments fetch first 10 rows only")

      for row in rows:
        print(row)
        rows_display.append(row)

      rows_display = tuple(rows_display)

      cur.close()

      return render_template("display.html", columns= columns, rows = rows_display, table= "tablename")
  return render_template("display.html")


@app.route("/insert1", methods = ['get', 'post'])
def insert1():
  
  return render_template('insert1.html')




@app.route("/insert1_table", methods = ['get', 'post'])
def insert1():
  
  if (request.method == 'POST'):
    id = request.form['text0']
    name = request.form['text1']
    bname = request.form['text2']
    lno = request.form['text3']
    pno = request.form['text4']
    city = request.form['text6']
    strt = request.form['text7']
    zip = request.form['text8']
    statecode = request.form['text9']
    state = request.form['text10']


    insert_stmt = "insert into Fall22_S004_14_Dealer (DealerID, Name, BusinessName, LicenseNumber, PhoneNumber, Commission, City, Street, Zipcode, StateCode, State) values ('" + id +"','"+ name + "','"+ bname + "','"+ lno + "','"+ pno + "','"+ str(5) + "','"+ city + "','"+ strt + "','"+ zip + "','"+ statecode +"','"+state +"')"

    try: 
        cur = connection.cursor()   
        cur.execute(insert_stmt)
        connection.commit()
    except Exception as e:
        print(e)

    cur2 = cur.execute('select dealerid from Fall22_S004_14_Dealer where dealerid = :dealerid', {'dealerid': id} )

    temp_row = []
    for row in cur2:
        temp_row.append(row[0])
    

    if (temp_row[0] == id):
        message = name + " Inserted into DB successfully"

    else:
        message =  "Unable to insert "+ name +" into DB"


    columns = cur.execute("select COLUMN_NAME from user_tab_columns where TABLE_NAME='FALL22_S004_14_DEALER'")
    
    cols = []

    for col in columns:
        cols.append(col[0])
    
    cols = tuple(cols)

    rows = cur.execute("select * from Fall22_S004_14_Dealer")
    row_li = []

    for row in rows:
        row_li.append(row)

    row_li = tuple(row_li)
    cur.close()

  return render_template("insert_data1.html", message = message, headings = cols,data = row_li, tablename = 'Fall22_S004_14_Dealer')



@app.route("/delete1", methods = ['get', 'post'])
def delete1():
  # insert 
  cur = connection.cursor()
  columns = cur.execute("select COLUMN_NAME from user_tab_columns where TABLE_NAME='FALL22_S004_14_PAYMENTS'")

  columns = []

  for col in columns:
      print("--col", col)
      columns.append(col[0])
  
  columns = tuple(columns)
  rows_display = []
  rows = cur.execute("select * from Fall22_S004_14_Payments fetch first 10 rows only")

  for row in rows:
    print(row)
    rows_display.append(row)

  rows_display = tuple(rows_display)


  print(columns)
  print(rows_display)


  cur.close()

  return render_template("delete1.html", columns= columns, rows = rows_display, table= "tablename")




if __name__ == '__main__':
   app.run(debug = True, port=5001)