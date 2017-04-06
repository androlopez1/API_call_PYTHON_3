import sqlite3

###THIS FUNCTION SHOWS THE CATEGORY TREE OF AN ID PROVIDED BY USER IN HTML FILE###
def create_HTML(x):
    conn = sqlite3.connect('categories_tree.db')
    c = conn.cursor()
    conn.commit
    x = input('Write ID: ',x)
    a = (str(x),)
    c.execute('select CategoryID, CategoryNAME, CategoryLEVEL, BestOffer from categories where CategoryParent =?',a)
    conn.commit
    if  c.fetchall():
        saveFile = open(str(x)+'.html','w')
        saveFile.write("<table style='text-align: center'><tr><th>Category id</th><th>Category name</th><th>Category level</th><th>Best Offer enabled</th></tr>")
        for row in c.execute('select CategoryID, CategoryNAME, CategoryLEVEL, BestOffer from categories where CategoryParent =?',a):
                saveFile.write('<tr><td>'+str(row[0])+'</td><td>'+str(row[1])+'</td><td>'+str(row[2])+'</td><td>'+str(row[3])+'</td></tr>')
        saveFile.write("</table>")
        saveFile.close()
        print ('HTML file succesfully created!')
    else:
        print('No Category Parent with ID: ', x)

create_HTML()
