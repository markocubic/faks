#!"C:\Users\Marko Ćubić\AppData\Local\Programs\Python\Python38-32\python.exe"
import cgi

print  ("""
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title></title>
	<meta name="Marko Cubic" content="">
	<link rel="stylesheet" href="styles.css">
</head>
<body>
    <form action="form2.py" method="post">
        <table>
            <tr>
                <td>Ime:</td>
                <td><input type="text" name="name"></td>
            </tr>
            <tr>
                <td>Lozinka:</td>
                <td><input type="password" name="psw"></td>
            </tr>
            <tr>
                <td>Ponovi lozinku:</td>
                <td><input type="password" name="pon-psw"></td>
            </tr>
            <tr>
                <td><input type="submit" value="Next"></td>
            </tr>
        </table>
    </form>
</body>
</html>
""")