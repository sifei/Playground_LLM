from huggingface_hub import snapshot_download

cache_dir = ".cache/huggingface/hub" # your cache directory
snapshot_download(repo_id='Pi3141/alpaca-native-7B-ggml', cache_dir=cache_dir)
