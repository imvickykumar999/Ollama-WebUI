from django.shortcuts import render
from .models import ChatMessage
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def chat_model(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        ChatMessage.objects.create(sender='user', message=user_message)

        # Example bot response
        bot_response = f"Echo: {user_message}"
        ChatMessage.objects.create(sender='bot', message=bot_response)

        return JsonResponse({"response": bot_response})
    return JsonResponse({"error": "Invalid method"}, status=400)

def chat_page(request):
    return render(request, 'chat/index.html')

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        if not user_message:
            return JsonResponse({'error': 'No message provided'}, status=400)

        try:
            process = subprocess.Popen(
                ["ollama", "run", "llama3.2"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            stdout, stderr = process.communicate(input=user_message)

            if process.returncode != 0:  # Check if the subprocess failed
                return JsonResponse({'error': f'Command failed: {stderr.strip()}'}, status=500)

            return JsonResponse({'response': stdout.strip()})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid method'}, status=400)
