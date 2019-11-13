#!"C:\Users\Marko Ćubić\AppData\Local\Programs\Python\Python38-32\python.exe"
import cgi
params = cgi.FieldStorage()

print('''
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title></title>
	<meta name="Marko Cubic" content="">
	<link rel="stylesheet" href="styles.css">
</head>
<body>
    <form action="vjezba3.py" method="post">
        <table>
            <tr>
                <td>Napomene:<textarea name="napomene" rows="10" cols="30">Prelazak na izvanredni studij.</textarea></td>
            </tr>
            <tr>
                <td><input type="submit" value="Next"></td>
                <td></td>
            </tr>
        
''')
print ('<input type="hidden" name="ime" value="' + params.getvalue("ime") + '">')    
print ('<input type="hidden" name="email" value="' + params.getvalue("email") + '">')    
print ('<input type="hidden" name="status" value="' + params.getvalue("status") + '">')    
print ('<input type="hidden" name="smjer" value="' + params.getvalue("smjer") + '">')  
print ('<input type="hidden" name="zavrsni" value="' + params.getvalue("zavrsni") + '">')
print('''   
        </table>
    </form>    
</body>
</html>     
''')
