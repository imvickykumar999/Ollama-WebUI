## `Ollama` : [Source](https://ollama.com/library/llama3.2)

[![image](https://github.com/user-attachments/assets/b7ae12bf-3e37-4a07-8425-6d71cd5e4430)](https://monkey-related-kangaroo.ngrok-free.app/)

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

## `WebUI` : [Blog](https://readmedium.com/geek-out-time-build-your-own-autonomous-ai-agent-backed-by-the-top-open-source-llm-deepseek-v3-and-9d04820f8f6d)

    Install:
        git clone https://github.com/browser-use/web-ui.git
        cd web-ui
        cp .env.example .env
        sudo snap install astral-uv --classic
        uv pip install -r requirements.txt
        playwright install

    Run:
        python webui.py --ip 127.0.0.1 --port 7788
