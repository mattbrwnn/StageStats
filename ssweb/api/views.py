from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    resp = {'Header': 'Test', 'response':200}
    return Response(resp)