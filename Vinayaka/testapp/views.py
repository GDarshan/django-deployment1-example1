from django.shortcuts import render


def index(request):
    context_dict = {'text':'helloworld','number':100}
    return render(request,'testapp/index.html',context_dict)

def other(request):
    return render(request,'testapp/other.html')

def relative(request):
    return render(request,'testapp/relative_url_template.html')
