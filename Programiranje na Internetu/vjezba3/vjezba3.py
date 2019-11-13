#!"C:\Users\Marko Ćubić\AppData\Local\Programs\Python\Python38-32\python.exe"
import cgi
form_data = cgi.FieldStorage()

ime = form_data.getvalue('ime')
email = form_data.getvalue('email')
status = form_data.getvalue('status')
smjer = form_data.getvalue('smjer')
zavrsni = form_data.getvalue('zavrsni')
napomene = form_data.getvalue('napomene')

def listToString(lista):  
    s = ""  

    for i in lista:  
        s += i 

    return s  
    
print ('''
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title></title>
	<meta name="Marko Cubic" content="">
	<link rel="stylesheet" href="styles.css">
</head>
<body>
    <form action="form1.py" method="post">
        <table>
            <tr>
                <td>Ime:</td>
                <td>
                ''')
print(ime)
print('''
                </td>
            </tr>
            <tr>
                <td>E-mail:</td>
                <td>
                ''')
print(email)
print('''
                </td>
            </tr>
            <tr>
                <td>Status:</td>
                <td>
                ''')
print(status)
print('''
                </td>
            </tr>
            <tr>
                <td>Smjer</td>
                <td>
                ''')
print(smjer)
print('''
                </td>
            </tr>
            <tr>
                <td>Zavrsni rad:</td>
                <td>
                ''')
try:
    a=listToString(zavrsni)
    print(a)
except Exception:
    print("Ne")
print('''
                </td>
            </tr>
            <tr>
                <td>Napomene:</td>
                <td>
                ''')
print(napomene)
print('''
                </td>
            </tr>       
        </table>
    </form>
    <a href="form1.py">Na pocetak</a>
</body>
</html>
''')






        