from django.shortcuts import render
from django.http import  HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')

def news_of_day(request):
    date = dt.date.today()
    day = convert_dates(date)
    html = f'''
         <html>
            <body>
                <h1>{day} {date.day}-{date.month}-{date.year}</h1>
            </body>
         </html>
          '''
    return HttpResponse(html)

def convert_dates(dates):
     # function to get the weekday number for a specific date

     day_number = dt.date.weekday(dates)

     days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

     day = days[day_number]
     return  day


