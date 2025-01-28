# `WebUI`

    git clone https://github.com/browser-use/web-ui.git
    cd web-ui
    cp .env.example .env
    sudo snap install astral-uv --classic
    uv pip install -r requirements.txt
    playwright install
    python webui.py --ip 127.0.0.1 --port 7788

# `Ollama`

    curl -fsSL https://ollama.com/install.sh | sh
    ollama run llama3.2
    ollama show llama3.2
    ollama list
    ollama ps
    ollama stop llama3.2
    ollama run llava "What's in this image? /home/vicky/Pictures/Screenshots/Screenshot.png"
