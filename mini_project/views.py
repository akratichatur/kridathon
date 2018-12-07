from django.shortcuts import render
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate,login,logout
 

# Create your views here.
#from django.http import HttpResponse



def result(request):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user inner join event on user.id=event.organiser_id WHERE user.id='1'")


 
'''
def index(request):
    display_user_data = User.objects.all()
    return render(request,"index.html",{'display_data': display_user_data})
 '''
def index(request):
    from django.db import connection, transaction
    cursor = connection.cursor()
    cursor.execute("UPDATE user SET username = 'Ananya' WHERE id = '2'")
    transaction.commit()

    # Data retrieval operation - no commit required
    cursor.execute("SELECT * FROM user inner join event on user.id=event.organiser_id WHERE user.id='1'")
    row = cursor.fetchone()
    return render(request,"index.html",{'display_data': row})

    '''messages.add_message(
        self.request,messages.SUCCESS,'Hello...Welcome to Kridathon')
     '''
 
    
'''
def my_custom_sql():
    from django.db import connection, transaction
    cursor = connection.cursor()

    # Data modifying operation - commit required
    cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
    transaction.commit_unless_managed()

    # Data retrieval operation - no commit required
    cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    row = cursor.fetchone()

    return row
'''
       



def FAQ(request):
    return render(request,"FAQ.html")

def about(request):
    return render(request,"about.html")

def game(request):
    return render(request,"game.html")

def event(request):
    return render(request,"event.html")

def tournament(request):
    return render(request,"tournament.html")

def athletics(request):
    return render(request,"athletics.html")

def badminton(request):
    return render(request,"badminton.html")

def basketball(request):
    return render(request,"basketball.html")


def chess(request):
    return render(request,"chess.html")


def cricket(request):
    return render(request,"cricket.html")


def football(request):
    return render(request,"football.html")


def handball(request):
    return render(request,"handball.html")

def volleyball(request):
    return render(request,"volleyball.html")


def hockey(request):
    return render(request,"hockey.html")


def summary(request):
    return render(request,"summary.html")

def join_event(request):
    return render(request,"join_event.html")

def organize_event(request):
    return render(request,"organize_event.html")

def join_tournament(request):
    return render(request,"join_tournament.html")

def organize_tournament(request):
    return render(request,"organize_tournament.html")
