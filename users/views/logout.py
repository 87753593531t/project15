from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, BlacklistMixin


from users.serializers import LogoutSerializer


class LogoutViewSet(APIView):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated, )


    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.logout_user(request, serializer.validate_data[''])
        return Response(data={'status':'true','details':'token in blacklist'}, status=status.HTTP_204_NO_CONTENT)
