#!"C:\Users\Marko Ćubić\AppData\Local\Programs\Python\Python38-32\python.exe"
import cgi
import os

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello Word - First CGI Program</title>')
print ('</head>')
print ('<body>')
print ('<h2>Hello Word! This is my first CGI program</h2>')
print ('</body>')
print ('</html>')

print  (os.environ)