# Fresh Installation

Read fresh installation instructions at https://github.com/eliranwong/biblemate/blob/main/docs/installation/macOS.md

## Additional Setup

### Set up virtual environment

For example:

```
cd
python3 -m venv biblemate
source biblemate/bin/activate
pip install --upgrade pip biblemate
export PATH=$PATH:$HOME/biblemate/bin
echo "export PATH=$PATH:$HOME/biblemate/bin" >> ~/.bashrc
biblemate
```

### Vertex AI Integration Support

Due to potential compatibility issues on some devices, the `google-genai` library is provided as a separate installation.

To use Vertex AI with BibleMate AI, install the required library:

> pip install --upgrade "biblemate[genai]"

### Upgrade

Run again:

> pip install --upgrade biblemate

### For Developer

> pip install -e .