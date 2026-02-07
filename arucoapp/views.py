# myapp/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import cv2

@api_view(['GET'])
def generate_aruco(request):
    # Get query parameters
    marker_id = int(request.GET.get('id', 0))
    marker_size = int(request.GET.get('size', 200))

    # Use modern OpenCV API
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_1000)
    marker_image = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)

    # Encode to PNG
    success, png_bytes = cv2.imencode('.png', marker_image)
    if not success:
        return Response({"error": "Failed to generate marker"}, status=500)

    return HttpResponse(png_bytes.tobytes(), content_type='image/png')
