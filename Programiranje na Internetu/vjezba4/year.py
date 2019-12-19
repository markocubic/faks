#!"C:\Users\Marko Ćubić\AppData\Local\Programs\Python\Python38-32\python.exe"

import structure
import session
import os
import cgi

params = cgi.FieldStorage()

godina = params.getvalue("godina")

if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)

data = session.get_session_data()

structure.start_html()
structure.print_navigation() 
structure.print_subjects_table(data, godina)
structure.finish_html()


