from datetime import date 
from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status

from .models import coupon 

class CouponValidationView(APIView):
    def post(self, request):
        code = request.data.get("code")

        try:
            coupon = Coupon.objects.get(
                code = code,
                is_active=True
            )

            today = date.today()

            if coupon .valid_from <=today <= coupon.valid_until:
                return Response(
                    {
                        "success": True,
                        "discount_percentage": coupon.discount_percentage
                    },
                    status=status.HTTP_200_OK
                )

            return Response(
                {
                    "success":False,
                    "massage": "Invalid coupon code"

                },
                status=status.HTTP_400_BAD_REQUEST

            )