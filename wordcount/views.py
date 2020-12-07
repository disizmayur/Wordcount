from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')


def count(request):
   text=request.GET['word']
   wordcount=text.split()
   ww={}
   for w in wordcount:
       if w in ww:
           ww[w] +=1
       else:
            ww[w]=1

   sorte=sorted(ww.items(),key=operator.itemgetter(1))
   return render(request,'c.html',{'text':text,'we':len(wordcount),'ww':sorte})

def about(request):
    return render(request,'about.html')