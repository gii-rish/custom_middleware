from django.http import HttpResponse

def testException(request):
    //this will throw an exception
    test = something
    return HttpResponse("Success")