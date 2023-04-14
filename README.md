# Playground_LLM

Alpaca_LoRA:https://github.com/tloen/alpaca-lora
```python generate.py --load_8bit --base_model 'decapoda-research/llama-7b-hf' --lora_weights 'tloen/alpaca-lora-7b'```

SSL Tunnel from remote server to local
```ssh -L 7860:localhost:7860 username@server```

Download ggml for embedding
see download_ggml.py

Generate sentence embedding
see create_embedding.py


Running Alpaca-lora:
```alpaca-lora]$ python generate.py --load_8bit --base_model 'decapoda-research/llama-7b-hf' --lora_weights 'tloen/alpaca-lora-7b''''

pref version
```
pip uninstall peft -y
pip install git+https://github.com/huggingface/peft.git@e536616888d51b453ed354a6f1e243fecb02ea08
'''
