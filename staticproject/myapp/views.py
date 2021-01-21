from django.shortcuts import render
def view1(request):
    myName="Rakshith"
    favPlayer="Dhoni"
    favAnimal="Lion"
    favSubject="Python"
    d={'name':myName,'player':favPlayer,'subject':favSubject,'animal':favAnimal}
    return render(request,'myapp/1.html',d)
