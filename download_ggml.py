from huggingface_hub import snapshot_download

cache_dir = ".cache/huggingface/hub" # your cache directory
snapshot_download(repo_id='Pi3141/alpaca-native-7B-ggml', cache_dir=cache_dir) # it has other model like for 13B, alpaca-lora version

