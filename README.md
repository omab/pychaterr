# PyChatErr

Python global error handler powered by ChatGPT to enhance errors resolutions.

# Description

PyChatErr installs a global exception handler that will send the cached
exception and related code to ChatGPT completion engine asking it to explain the
issue and propose solutions.

# Installation

Install using `pip`:

```shell
pip install pychaterr
```

# Usage

This module requires a OpenAI API Key:

1. Generate a key at https://platform.openai.com/account/api-keys
2. Export it with:
   ```
   export OPENAPI_API_KEY=sk-...
   ```

Then import the module in your code with:

```python
import pychaterr
```

# Demo

[![asciicast](https://asciinema.org/a/as6OC8KH0Oe6w78Yw10TexmsV.svg)](https://asciinema.org/a/as6OC8KH0Oe6w78Yw10TexmsV)

# Examples

The [examples/](examples/) folder contains examples showing this module behavior.

Run the samples with:

```shell
# Create and activate a virtual environment
pip install -e .
python examples/zerodivision.py
```

# License

See [LICENSE](LICENSE) file for details.