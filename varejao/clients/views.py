from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Contacts
from .serializers import ContactSerializer

class ContactList(APIView):
    """
    List all Contacts or create a new Contact
    """
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        queryset = Contacts.objects.all()
        serializer = ContactSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            contacts = []
            for contact in request.data['contacts']:
                n = Contacts()
                n.nome = contact['name']
                n.celular = contact['cellphone']
                n.save()
                contacts.append(n)
            serializer = ContactSerializer(contacts, many=True)
        except KeyError:
            try:
                contact = Contacts()
                contact.nome = request.data['name']
                contact.celular = request.data['cellphone']
                contact.save()
                serializer = ContactSerializer(contact, many=False)
            except KeyError:
                return Response(
                    {"msg": "Erro: os parâmetros não correspondem aos esperados pela API."}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.data)
