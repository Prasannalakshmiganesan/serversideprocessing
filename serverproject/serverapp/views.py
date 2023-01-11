from django.shortcuts import render

# Create your views here.
def area(request):
    context= {}
    context['length']="0"
    context['width']="0"

    if request.method == 'POST':
        print("POST METHOD IS USED")
        length=request.POST.get("length",0)
        width=request.POST.get("width",0)
        print('Length=',length)

        print('Width=',width)

        length_num = int(length)
        width_num = int(width)
        area=length_num*width_num
        context['length']=length
        context['width']=width
        context['area']=area
        print('Area=',area)
        
    return render(request,"serverapp/area.html",context)

def cssstyle(request):
    return render(request, "serverapp/cssstyle.html")