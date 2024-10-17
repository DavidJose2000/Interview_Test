from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# ****** importing model and serializer ********
from . models import Expense
from .serializers import ExpensesSerializers


class ExpensesApiView(APIView):
    # GET method handling
    def get(sefl, request):
        expenses = Expense.objects.all()
        serializer = ExpensesSerializers(expenses, many=True)
        return Response(serializer.data)

    
    # Post method handling
    def post(self, request):
        print("post Activated")
        data = request.data
        serializer = ExpensesSerializers(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        
