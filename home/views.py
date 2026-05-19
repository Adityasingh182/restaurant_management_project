from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializers_class = MenuCategorySerializer
# Create your views here.
