from django.db import models
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage
import subprocess

def chat_page(request):
    messages = ChatMessage.objects.all().order_by('timestamp')  # Load all messages in order
    return render(request, 'chat/index.html', {'messages': messages})

@csrf_exempt
def chat_api(request):
    if request.method == 'GET':  # Fetch saved messages
        messages = ChatMessage.objects.all().order_by('timestamp')
        messages_data = [
            {"sender": msg.sender, "message": msg.message, "timestamp": msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
            for msg in messages
        ]
        return JsonResponse({"messages": messages_data})

    if request.method == 'POST':  # Send and store new messages
        user_message = request.POST.get('message', '').strip()
        if not user_message:
            return JsonResponse({'error': 'No message provided'}, status=400)

        ChatMessage.objects.create(sender="User", message=user_message)  # Save user message

        try:
            process = subprocess.Popen(
                ["ollama", "run", "blogforge"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                encoding="utf-8",
                text=True,
            )
            stdout, stderr = process.communicate(input=user_message)

            if process.returncode != 0:
                return JsonResponse({'error': f'Command failed: {stderr.strip()}'}, status=500)

            bot_response = stdout.strip()
            ChatMessage.objects.create(sender="Bot", message=bot_response)  # Save bot message

            return JsonResponse({'response': bot_response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid method'}, status=400)
