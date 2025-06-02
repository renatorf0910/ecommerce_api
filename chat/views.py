from openai import OpenAI
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

from products.models import Product

client = OpenAI(api_key=settings.OPENAI_API_KEY)

class ChatProductAPIView(APIView):
    def post(self, request):
        user_message = request.data.get("message", "")

        produtos = Product.objects.all()[:10]

        contexto_produtos = "\n".join([
            f"- {p.nome} (R${p.preco}): {p.descricao}" for p in produtos
        ])

        system_prompt = (
            "Você é um assistente de um e-commerce. "
            "Sugira produtos conforme o pedido do cliente. "
            "Aqui estão os produtos disponíveis:\n" + contexto_produtos
        )

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.choices[0].message.content.strip()
        return Response({"reply": reply})
