from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from . import models, serializers


@api_view(['GET'])
def get_from_ifsc(request):
    """
    This api view will return all the details of the branch given it's IFSC code.
    """
    q = request.GET.get('q') if request.GET.get('q') else request.data.get('q')
    if q:
        try:
            branch = models.Branch.objects.get(ifsc_code=q, is_deleted=False)
            serializer = serializers.BranchSerializer(branch)
            return Response({
                "status": "OK",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except:
            raise NotFound
    return Response({
        "status": "OK",
        "message": "provide 'q' parameter as IFSC code of the branch and we will give you details."
    }, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def get_branches(request):
    """
    This api view will return all the branches given it's bank name and city name.
    """
    if request.method == 'POST':
        bank_name = request.GET.get('bank_name') if request.GET.get('bank_name') else request.data.get('bank_name')
        city_name = request.GET.get('city_name') if request.GET.get('city_name') else request.data.get('city_name')
        if city_name and bank_name:
            try:
                branches = models.Branch.objects.filter(
                    is_deleted=False, bank__name=bank_name, location__city=city_name
                )
                serializer = serializers.BranchSerializer(branches, many=True)
                return Response({
                    "status": "OK",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            except:
                raise NotFound
    return Response({
        "status": "OK",
        "message": "provide 'bank_name' parameter as bank name and 'city_name' parameter"
                   "as city name and we will give you branches."
    }, status=status.HTTP_200_OK)
