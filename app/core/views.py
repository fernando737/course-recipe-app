"""
Core views for app
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def healt_check(request):
    """Returns successfull response."""
    return Response({'status': 'ok'})