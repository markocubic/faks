#!"C:\Users\Marko Ćubić\AppData\Local\Programs\Python\Python38-32\python.exe"
import cgi
params = cgi.FieldStorage()
first_name = params.getvalue("firstname")

print ('''
<!DOCTYPE html>
<html>
<body>

<h2>Odaberite smjer:</h2>

<form action="test4.py" method="post">
  <select name="smjer_studija">
    <option value="programiranje">programiranje</option>
    <option value="baze_podataka">baze podataka</option>
    <option value="mreze">mreze</option>
    <option value="informacijski_sustavi">informacijski sustavi</option>
  </select>
  <br><br>''')
print ('<input type="hidden" name="ime" value="' + params.getvalue("firstname") + '">')
print ('''
<br>
<input type="submit" value="submit">
</form>

</body>
</html>''')
#print (params.getvalue("firstname"))
#print ('<br>')
print (params.getvalue("ime"))
