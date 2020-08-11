from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html',{'hithere':'This is me'})


def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    sortedwrds = sorted(worddict.items(),key = operator.itemgetter(1),reverse = True)
    return render(request,'count.html',{'Fulltext': fulltext,'count':len(wordlist),'sortedwrds':sortedwrds })

def about(request):
    return render(request,'about.html')