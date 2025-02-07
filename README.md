# `Quick Start`

```bash
python manage.py runserver
ngrok http --url=free-camel-deadly.ngrok-free.app 8000

# in seperate terminal
ollama serve

python app.py
python generate.py

ollama create blogforge -f ./Modelfile
OLLAMA_USE_CUDA=1 ollama run blogforge
```

>## `Custom Model`
>
>![image](https://github.com/user-attachments/assets/0049f332-f543-4d17-8edb-5898ac531bd4)

## `Ollama` : [`Source`](https://ollama.com/library/llama3.2)

```bash
Install:
    curl -fsSL https://ollama.com/install.sh | sh
    
Run:
    ollama serve
    ollama run llama3.2
    
More:
    ollama show llama3.2
    ollama list
    ollama ps
    ollama stop llama3.2
    ollama run llava "What's in this image? /home/Vicky/Pictures/Screenshot.png"
```

>[![image](https://github.com/user-attachments/assets/a33b9e1a-b824-47b2-9259-f78d588e727a)](https://shiny-tribble-vqjxv5jp7w6hw6r-4040.app.github.dev/inspect/http)
>[![image](https://github.com/user-attachments/assets/5427ca16-4477-424f-b2d8-f7ef6b097b6f)](https://free-camel-deadly.ngrok-free.app/)

## WebUI : [Blog](https://readmedium.com/geek-out-time-build-your-own-autonomous-ai-agent-backed-by-the-top-open-source-llm-deepseek-v3-and-9d04820f8f6d)

```bash
sha256sum Anaconda3-2024.10-1-Linux-x86_64.sh
bash Anaconda3-2024.10-1-Linux-x86_64.sh
source ~/.bashrc
conda init
git clone https://github.com/browser-use/web-ui.git
cd web-ui/
conda info --env
conda activate base
pip install -r  requirements.txt
playwright install
python webui.py --ip 127.0.0.1 --port 7788
```
