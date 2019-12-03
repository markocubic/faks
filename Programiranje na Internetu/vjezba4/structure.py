#!"C:\Users\Marko Ćubić\AppData\Local\Programs\Python\Python38-32\python.exe"

import model

def start_html():
    print('''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>vjezba4</title>
        <meta name="Marko Cubic" content="">
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
    ''')

def print_navigation():
    print ('''
    <form action="" method="post">
    <div id="navigation">
        <input type="submit" class="button" name="godina" value="Godina 1" formaction="year.py">
        <input type="submit" class="button" name="godina" value="Godina 2" formaction="year.py">
        <input type="submit" class="button" name="godina" value="Godina 3" formaction="year.py">
        <input type="submit" class="button" value="Upisni list" formaction="list_all.py">
    </div>''')     

def print_subjects_table(data, year):
    year = model.listToString(year)

    print("<table>")
    print("<tr class='top-year'><td colspan ='3'>", year,"</td></tr>")
    print("<tr class='top'><td>Predmet</td><td>Status</td><td>Bodovi</td></tr>")
    
    subjects = model.get_subjects()
    
    for key, subject in subjects.items():
        subject_year = subject.get('year', 'n/a')

        if str(subject_year) == year[7]:
            checked1 = checked2 = checked3 = ""
            subject_name = subject.get('name', 'n/a')
            subject_ects = subject.get('ects', 'n/a')

            status = model.check_status(data, key)

            if status == "Ne upisuje":
                checked1 = "checked"
            elif status == "Upisuje":
                checked2 = "checked"
            elif status == "Polozen":
                checked3 = "checked"
            
            print("""
            <tr>
                <td>""", subject_name,"""</td>
                <td>
                    <input type='radio' name=""", str(key),""" value='Ne upisuje'"""
                        , checked1,""">Ne Upisuje
                    <input type='radio' name=""", str(key),""" value='Upisuje'"""
                        , checked2,""">Upisuje
                    <input type='radio' name=""", str(key),""" value='Polozen'"""
                        , checked3,""">Polozen
                </td>
                <td>""", subject_ects,"""</td>
            </tr>
            """)
    print("</table>")

def print_listall_table(data):
    print("<table>")
    print("<tr class='top'><td>Predmet</td><td>Status</td><td>Bodovi</td></tr>")
    
    subjects = model.get_subjects()
    for subject_id, status in data.items():
        subject_name = subjects.get(subject_id, {}).get("name", "n/a")
        subject_ects = subjects.get(subject_id, {}).get("ects", "n/a")
        print ("<tr><td>", subject_name,"</td><td>", str(status),"</td><td>"
            , subject_ects,"</td></tr>")
    print("</table>")

def finish_html():
    print('''
    </form>
    </body>
    </html>
    ''')