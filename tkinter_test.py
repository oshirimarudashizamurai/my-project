import tkinter as tk
import tkinter.ttk as ttk
import psycopg2

con = psycopg2.connect(host='localhost',
                      user='postgres',
                      password='admin',
                      database='mydb')

def createitemname():
    with con.cursor() as cur:
        cur.execute("select item_name from item")
        li = cur.fetchall()
        return(li)
def create_sql(item_name):
    with con.cusor() as cur:
        cur.execute("select item_code from item where item_name = %s",(item_name))
        item_code = cur.fetchone()[0]
    acc_data = entry1.get()
    amount =entry3.get()
    try:
        with con:
            with con.cursor() as cursor:
                sql = "insert into acc_table(acc_data,item_code,amount) VALUES(%s,%s,%s)"
                cursor.execute(sql,(acc_data,item_code,amount))

                con.commit()
                print("1件登録しました")
    except:
        print("エラーのため登録できませんでした。")

root = tk.Tk()
root.title('家計簿')

root.geometry("300x300")

frame = tk.Frame(root,bd=3,relief="ridge")
frame.pack(fill="x")

button1 = tk.Button(frame,text="入力",bg="blue")
button1.pack(side="left")
button2 = tk.Button(frame,text="表示",bg="blue")
button2.pack(side="left")
button3  = tk.Button(frame,text="終了",bg="red")
button3.pack(side="right")

label1 = tk.Label(root,text="【入力画面】",font=16)
label1.pack(fill="x")

frame1 = tk.Frame(root,pady=10)
frame1.pack()
label2 =tk.Label(frame1,font=("",14),text="日付")
label2.pack(side="left")
entry1 = tk.Entry(frame1,font=("",14),justify="center",width=15)
entry1.pack(side="left")

frame2 = tk.Frame(root,pady=10)
frame2.pack()
label3 = tk.Label(frame2,font=("",14),text="内訳")
label3.pack(side="left")

combo = ttk.Combobox(frame2, state='readonly', font=("",14),width=13)
combo["values"] = createitemname()
combo.current()
combo.pack()

frame3 = tk.Frame(root,pady=10)
frame3.pack()
label4 = tk.Label(frame3,font=("",14),text="金額")
label4.pack(side="left")
entry3 = tk.Entry(frame3,font=("",14),justify="center",width=15)
entry3.pack(side="left")

button4 = tk.Button(root,text="登録",font=("",16),width =10,bg="grey",command=lambda:create_sql (combo.get()))
button4.pack()

root.mainloop()