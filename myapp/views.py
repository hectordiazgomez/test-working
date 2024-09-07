from django.http import JsonResponse

def get_details(request):
    if request.method == "GET":
        return JsonResponse({"Hola": "Api funcionando"})