
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
import sqlite3
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

# c.execute("""CREATE TABLE details(
#          Username text,
#          Password text
#           )""")
# c.execute("INSERT INTO details VALUES ('disha','abc')")
# c.execute("INSERT INTO details VALUES ('bob','456')")

# c.execute("SELECT Password FROM details where Username=?",(usr,))
#
# if(c.rowcount!=0):
#     l = c.fetchone()
#     passw=l[0]
#     if (passw == 'abc'):
#         print("You are logged in !")
# else:
#     print("Username doesnt exist")
#conn.commit()



def index(request):
    return HttpResponse("First Page of Django Project !")

def Display_date_time(request):
    da=datetime.datetime.now()
    return render_to_response('firstwebapp/firstpage.html', {'da': da})

@csrf_exempt
def login_form(request):
    try:
        conn = sqlite3.connect('login.db')
        c = conn.cursor()
        if request.method == 'POST':
             usr = request.POST.get("usrname")
             password = request.POST.get("password")
             print(usr)
             print(password)
             c.execute("SELECT Password FROM details where Username=?", (usr,))

             if(c.rowcount!=0):
                l = c.fetchone()
                passw=l[0]
                if (passw == password):
                    print("You are logged in !")
                    return HttpResponseRedirect('/home/')
                else:
                    #password invalid
                    return HttpResponseRedirect('/invalid/')
             else:
                #username invalid
                return HttpResponseRedirect('/invalid/')
        else:
            print("Invalid Request!")

    except:
        print("Exception here")
        return HttpResponseRedirect('/invalid/')
    
    conn.commit()
    conn.close()

    return render_to_response('firstwebapp/firstpage.html')


def home_page(request):
    return render_to_response('firstwebapp/login.html')

def invalid_login(request):
    return render_to_response('firstwebapp/invalid.html')

