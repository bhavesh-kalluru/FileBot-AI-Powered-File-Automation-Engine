# FileBot – AI‑Powered File Automation Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/filebot.svg)](https://pypi.org/project/filebot/)

An intelligent, GenAI‑driven file management assistant that automates organization, tagging, and retrieval across local and cloud storage.

---

## Table of Contents

* [Features](#features)
* [Getting Started](#getting-started)

  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)

  * [Command‑Line Interface](#command-line-interface)
  * [Python API](#python-api)
* [Configuration](#configuration)
* [Extensible Plugins](#extensible-plugins)
* [Contributing](#contributing)
* [Roadmap](#roadmap)
* [License](#license)
* [Contact](#contact)

---

## Features

* **Smart Classification**
  Uses custom ML models to categorize documents by content, context, and metadata.

* **Natural‑Language Search**
  Find any file simply by describing it in plain English.

* **Cross‑Platform Sync**
  Seamless integration with Windows, macOS, Linux, and popular cloud drives (Google Drive, Dropbox, OneDrive).

* **Extensible Plugin System**
  Easily add connectors and custom workflows via modular plugins.

* **Secure & Private**
  All indexing and inference runs locally; no file contents are shared externally without your consent.

---

## Getting Started

### Prerequisites

* Python 3.9 or higher
* `git` (for cloning the repo)
* Optional: credentials for cloud‑storage APIs (see [Configuration](#configuration))

### Installation

```bash
# From PyPI
pip install filebot

# From source
git clone https://github.com/your-username/filebot.git
cd filebot
pip install -r requirements.txt
```

---

## Usage

### Command‑Line Interface

```bash
# Initialize FileBot in the current directory
filebot init

# Index all files and subfolders
filebot index --path /path/to/data

# Search by natural-language query
filebot search "presentation deck about Q2 revenue"

# Sync with cloud storage
filebot sync --service google_drive
```

Run `filebot --help` for full list of commands and options.

### Python API

```python
from filebot import FileBot

# Create a FileBot instance
bot = FileBot(config_path="~/.filebot/config.yml")

# Index a folder
bot.index("/Users/bhav/Documents")

# Search for files
results = bot.search("find draft of project proposal")
for file in results:
    print(file.path, file.score)
```

---

## Configuration

FileBot uses a YAML config file to store credentials and preferences:

```yaml
# ~/.filebot/config.yml
storage:
  local: true
  google_drive:
    enabled: true
    client_id: YOUR_CLIENT_ID
    client_secret: YOUR_CLIENT_SECRET

model:
  name: "custom-transformer-v1"
  confidence_threshold: 0.75
```

---

## Extensible Plugins

Add support for new storage backends or custom workflows:

1. Create a new plugin module under `filebot/plugins/`
2. Extend the `BaseConnector` or `BaseWorkflow` class
3. Register your plugin in `filebot/plugins/__init__.py`

```python
from filebot.plugins import BaseConnector

class S3Connector(BaseConnector):
    name = "s3"
    def authenticate(self, **creds):
        # implement AWS S3 auth
        ...

    def list_files(self, path):
        # list objects in S3 bucket
        ...
```

---

## Contributing

We welcome contributions! Please:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/awesome-plugin`)
3. Commit your changes (`git commit -m "Add awesome plugin"`)
4. Push to your branch (`git push origin feature/awesome-plugin`)
5. Open a Pull Request

Be sure to run tests and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

---

## Roadmap

* [ ] GUI dashboard for visualization
* [ ] Native mobile (iOS/Android) companion apps
* [ ] Advanced rule‑based automation workflows

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contact

Maintainer: Bhavesh Kalluru
Email:kallurubhavesh341@gmail.com
LinkedIn: https://www.linkedin.com/in/bhaveshkalluru/
