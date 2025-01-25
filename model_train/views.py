import csv

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

from .models import CustomerData
from .serializers import CustomersSerializer
from rest_framework.response import Response

from .train_process import train_model


class CustomerListView(ListAPIView):
    """
    API view to retrieve a customers list.
    """
    queryset = CustomerData.objects.all()
    serializer_class = CustomersSerializer


class UploadCSVView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file', None)

        if not file:
            return Response({"error": "No file provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Decode the uploaded file
            decoded_file = file.read().decode('utf-8')
            reader = csv.DictReader(decoded_file.splitlines())

            customers = []
            for row in reader:
                # Create Customer instances but don't save yet
                customers.append(
                    CustomerData(
                        age=row['age'],
                        experience=row['experience'],
                        income=row['income'],
                        zip_code=row['zip_code'],
                        family=row['family'],
                        ccavg=row['ccavg'],
                        education=row['education'],
                        mortgage=row['mortgage'],
                        personal_loan=bool(int(row['personal_loan'])),
                        securities_account=bool(int(row['securities_account'])),
                        cd_account=bool(int(row['cd_account'])),
                        online=bool(int(row['online'])),
                        creditcard=bool(int(row['creditcard'])),
                    )
                )

            # Bulk create all customers
            CustomerData.objects.bulk_create(customers)

            return Response({"message": "CSV file processed successfully."}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class TrainModelView(APIView):
    train_model()


class PredictModelView(APIView):
    pass
