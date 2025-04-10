# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework.decorators import api_view
from rest_framework.response import Response
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@api_view()
def home(request):
    return Response({
        'status': 200,
        'message': "Welcome to the DripDrop Django REST Framework API"
        })

# dj-rest-auth logout view fix
@api_view(['POST'])
def logout_route(request):