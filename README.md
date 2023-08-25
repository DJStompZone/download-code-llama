![](https://i.imgur.com/eumqBOu.png)

# Download Code Llama Models with Python

This Python script provides a quality-of-life enhancement for downloading [Code Llama](https://github.com/facebookresearch/codellama) models. Rather than relying on manual methods or the typical wget command, users can utilize this script to streamline the download process.


## Features
- Interactive CLI: Prompt-based interface for selecting which models to download.
- Progress Bar: Visual progress indicator for active downloads thanks to tqdm.
- Checksum Verification: Ensures data integrity by checking the downloaded files against provided checksums.
- Flexible URL Input: Adaptable to various URLs, provided they follow the expected pattern.


## Prerequisites
Python 3.x
Required Python packages: httpx, tqdm
You can install these via pip:
```bash
pip install httpx tqdm
```


## Usage
- Clone this repository:
  ```bash
  git clone https://github.com/DJStompZone/download-code-llama/
  cd download-code-llama
  ```

- Run the script:
  ```bash
  python download.py
  ```

- Follow the on-screen prompts. You'll be asked to:

  - Provide the download URL. (You can get one [here](https://ai.meta.com/resources/models-and-libraries/llama-downloads/))
  - Select specific models or download all available models.
  The script will download the selected models to the current directory (or the specified directory) and verify them using the provided checksums.

### Notes
If you encounter any server-side restrictions, remember to respect any terms of service or usage policies associated with the resources you're accessing. This script aims to simplify the download process but should not be used in any context that violates the [Acceptable Use Policy](https://ai.meta.com/llama/use-policy/).
