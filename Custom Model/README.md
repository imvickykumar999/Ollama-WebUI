# **Custom Model** : _`sitemap.xml`_

```bash
curl -fsSL https://ollama.com/install.sh | sh

# 1st termux session
ollama serve

# 2nd termux session
python app.py
python generate.py

ollama create blogforge -f ./Modelfile
OLLAMA_USE_CUDA=1 ollama run blogforge
```
## _`Modelfile`_

```txt
FROM llama3.2:1b

# set the temperature to 1 [higher is more creative, lower is more coherent]
PARAMETER temperature 1

# set the system message
SYSTEM """
(Your website FAQ generated from generate.py)
"""
```

## _`views.py`_

```py
process = subprocess.Popen(
    ["ollama", "run", "blogforge"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    encoding="utf-8",
    text=True,
    env={**os.environ, "OLLAMA_USE_CUDA": "1"}
)
```
