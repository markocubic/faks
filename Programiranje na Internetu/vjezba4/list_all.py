#!"C:\Users\Marko Ćubić\AppData\Local\Programs\Python\Python38-32\python.exe"

import structure
import session
import os
import cgi

params = cgi.FieldStorage()

if (os.environ["REQUEST_METHOD"].upper() == "POST"):
    session.add_to_session(params)

data = session.get_session_data()

print()
structure.start_html()
structure.print_navigation()
structure.print_listall_table(data)
structure.finish_html()