#!"C:\Users\Marko Ćubić\AppData\Local\Programs\Python\Python38-32\python.exe"

import structure
import session

data = session.get_session_data()

print()
structure.start_html()
structure.print_navigation() 
structure.finish_html()


