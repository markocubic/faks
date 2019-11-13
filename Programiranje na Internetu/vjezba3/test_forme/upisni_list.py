#!"C:\Users\Marko Ćubić\AppData\Local\Programs\Python\Python38-32\python.exe"
import cgi
form_data = cgi.FieldStorage()

print('')
print (form_data.getvalue(''))
print (form_data.getvalue('ime'))
print (form_data.getvalue('smjer'))

