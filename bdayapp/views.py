from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    return render(request,'index.html')
def calc(request):
    if request.method=='POST':
      
        Date=request.POST.get('Date')
        year=request.POST.get('year')
        Month=request.POST.get('Month')
        today=datetime.date.today()
        birthday=datetime.date(int(year),int(Month),int(Date))
        days=(today-birthday).days

    return render(request,'index.html',{"days":days})

    
  
  

