import os
import httpx
import hashlib
from tqdm import tqdm
from typing import List
from motd import show_banner
from time import sleep

class DownloadManager:
    def __init__(self, url, selected_models: List[str] = [""], download_dir="."):
        self.url = url
        self.selected_models = selected_models
        self.download_dir = download_dir
        self.models = [f"{s}{t}" for s in ["7b", "13b", "34b"] for t in ["", "-Python", "-Instruct"]]
        self.model_to_shard_dict = {ea: ((int(ea.split('b')[0])-6) % 5) - 1 for ea in self.models}
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_6 HTTP/1.0 200 9644 335 0 - Wget/1.12 (linux-gnu)"}
        if not self.selected_models:
            self.selected_models = self.models
        os.makedirs(self.download_dir, exist_ok=True)

    def model_to_shard(self, model):
        return self.model_to_shard_dict.get(model, None)


    def download_file(self, filename, model=None, size=None):
        """Download a file with a progress bar if size is provided and extension is .pth."""
        model_path = f"CodeLlama-{model}"
        normalized_filename = os.path.join(model_path, filename) if model else filename
        filepath = os.path.join(self.download_dir, normalized_filename)
        url = self.url.replace('*', f"{model_path}/{filename}" if model else filename)
        with self.client.stream("GET", url, headers=self.headers, timeout=None) as response, open(filepath, "wb") as f:
            if size and filename.endswith('.pth'):
                with tqdm(total=size, unit='B', unit_scale=True, desc=filename, unit_divisor=1024) as pbar:
                    for chunk in response.iter_bytes(chunk_size=1024*1024):
                        f.write(chunk)
                        pbar.update(len(chunk))
            else:
                for chunk in response.iter_bytes():
                    f.write(chunk)


    def checksum(self, directory):
        """Verify files using the checksum."""
        if not os.path.isfile(os.path.join(directory, "checklist.chk")):
            print(f"File {os.path.join(directory, 'checklist.chk')} not found.")
            return False
        with open(os.path.join(directory, "checklist.chk"), 'r') as f:
            lines = f.readlines()
            for line in lines:
                chksum, filename = line.strip().split('  ')
                file_path = os.path.join(directory, filename)
                if not os.path.exists(file_path):
                    print(f"File {filename} not found.")
                    return False
                with open(file_path, 'rb') as file:
                    md5 = hashlib.md5(file.read()).hexdigest()
                    if md5 != chksum:
                        print(f"Checksum mismatch for {filename}. Expected: {chksum}, Got: {md5}")
                        return False
        return True


    def download_model(self, model):
        """Download an individual model"""
        model_path = f"CodeLlama-{model}"
        print(f"Downloading CodeLlama-{model}")
        model_directory = os.path.join(self.download_dir, model_path)
        os.makedirs(model_directory, exist_ok=True)

        for s in range(self.model_to_shard(model) + 1):
            self.download_file(f"consolidated.{s:02}.pth", model, size=16477776)
        self.download_file("params.json", model)
        self.download_file("tokenizer.model", model)
        self.download_file("checklist.chk", model)
        
        print("Checking checksums")
        if not self.checksum(model_directory):
            print(f"Checksum verification failed for CodeLlama-{model}")
            return False
        print("Checksums verified")
        return True


    def download_models(self):
        """Download all selected models"""
        with httpx.Client() as self.client:
            self.download_file("LICENSE")
            self.download_file("USE_POLICY.md")
            for model in self.selected_models:
                self.download_model(model)

if __name__ == "__main__":
    show_banner()
    url = input("Enter the URL from email: ")
    selected_models = input(f"Enter the list of models to download without spaces, or press Enter for all: ")
    downloader = DownloadManager(url, selected_models.replace(" ", '').split(','))
    downloader.download_models()
