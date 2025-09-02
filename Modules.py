import mysql.connector as mys
passwd=input("Enter your mysql password")
database=mys.connect(host="localhost",
          user="root",
          passwd=passwd,
          database="todoo")
curs=database.cursor()
def CreateTable(name):
    todorec=curs.execute(f'''create table {name}(
                         subject varchar(20),
                         Date_of_commencing date)''')
    database.commit()
    database.close()
    return 0
def ValueInsert(n):
    for i in range(int(n)):
        subject=input("Enter subject name")
        date=input("Enter date with hyphens YYYY-MM-DD")
        query=f"""insert into test
                  values('{subject}','{date}')"""
        print("values have been inserted successfully")
        curs.execute(query)
    return 0
def Viewer():
    coulumn=""
    choice=int(input("What do you want to view from the table\n1.Subject\n2.Date_of_commencing"))
    if choice==1:
       coulumn="subject"
    elif choice==2:
        coulumn="Date_of_commencing"
    curs.execute(f"Select {coulumn} from test")
# print("WHAT DO YOU WANT TO DO?")
# print("---------------------------")
# choice=int(input("1.create table\n2.Enter value\n3.View\n4.exit"))
# i=0
# while i<1:
#     if choice==1:
#         CreateTable()
#     elif choice==2:
#         n = int(input("How many values do you want to enter"))
#         ValueInsert(n)
#     elif choice==3:
#         Viewer()
#     elif choice==4:
#         i+1
#     choice=int(input("1.create table\n2.Enter value\n3.View\n4.Exit"))
# database.commit()
# database.close()