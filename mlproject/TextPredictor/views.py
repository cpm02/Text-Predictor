from django.http import HttpResponse
from django.shortcuts import render
from . import text_pred

def homepage(request):
    # return render(request,'homea.html')
    return render(request,'homepage.html')

def result(request):
    djtext=request.POST.get('text','default')
    ans=text_pred.Bgen(djtext)
    pred=ans.split()
    print(pred[0])
    Prediction={'data1': pred[0],'data2': pred[1],'data3': pred[2],'data4': pred[3],'data5': pred[4],'ans':djtext}
    return render(request, 'result.html',Prediction )




# def ana(request):
#     djtext=request.POST.get('text','default')
#     Politics=request.POST.get('Politics','off')
#     Business=request.POST.get('Business','off')
#     Tech=request.POST.get('Tech','off')
#     Sports=request.POST.get('Sports','off')
#     Entertainment=request.POST.get('Entertainment','off')
    
#     params = {'purpose': 'predicted', 'analyzed_text': 'default'}
    
#     # print(len(djtext))
#     # input_string=len(djtext.split())
#     # print(input_string)
#     if(Business=="on"):
#         # ans=djtext
#         # ans=ans+" "+text_pred.Bgen(djtext)
#         # pred=text_pred.gen(djtext)
#         ans=text_pred.gen(djtext)
#         pred=ans.split
#         print(pred[0])
        


#         params = {'purpose': 'Predicted', 'analyzed_text': ans}
#         print("Business run")

        
#     elif Tech=="on":
#             ans=djtext
#             ans=ans+" "+text_pred.Tgen(djtext)
#             print("Tech run")
#             pred=text_pred.gen(djtext)
            
#             params = {'purpose': 'predicted', 'analyzed_text': ans}
#     elif Sports=="on":
#             ans=djtext
#             ans=ans+" "+text_pred.Sgen(djtext)
#             print("Sports run")

#             # pred=text_pred.gen(djtext)
#             params = {'purpose': 'predicted', 'analyzed_text': ans}
#     elif Entertainment=="on":
#             ans=djtext
#             ans=ans+" "+text_pred.Egen(djtext)
#             print("Entertainment run")
#             # pred=text_pred.gen(djtext)
#             params = {'purpose': 'predicted', 'analyzed_text': ans}
#     elif Politics=="on":
#             ans=djtext
#             ans=ans+" "+text_pred.Pgen(djtext)
#             print("Politics run")
#             # pred=text_pred.gen(djtext)
#             params = {'purpose': 'predicted', 'analyzed_text': ans}
           
#     return render(request, 'ana.html', params)

