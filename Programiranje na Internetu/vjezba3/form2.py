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
    <form action="form3.py" method="post">
        <table>
            <tr>
                <td>Status:</td> 
                <td>
                    <input type="radio" name="status" value="Redovan" checked>Redovan
                    <input type="radio" name="status" value="Izvanredan">Izvanredan
                </td>
            </tr>
            <tr>
                <td>E-mail:</td>
                <td><input type="text" name="email"></td>
            </tr>
            <tr>
                <td>Smjer:</td>
                <td>
                    <select name="smjer">
                        <option value="baze">Baze Podataka</option>
                        <option value="info">Informacijski Sustavi</option>
                        <option value="lin">Linearna Algebra</option>
                        <option value="pni">Programiranje na Internetu</option>
                    </select> 
                </td>
            </tr>
            <tr>
                <td>Zavrsni:</td>
                <td>
                    
                    <input type="checkbox" name="zavrsni" value="Da ">
                </td>
            </tr>
            <tr>
                <td><input type="submit" value="Next"></td>
                <td></td>
            </tr>
''')
print ('<input type="hidden" name="ime" value="' + params.getvalue("name") + '">')
print('''
        </table>
    </form>
</body>
</html>
''')