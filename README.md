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

Simply importing the module into your code will define the exception handler:

```python
import pychaterr
```

# Examples

The [examples/] folder contains examples showing this module behavior.

Run the samples with:

```shell
# Create and activate a virtual environment
pip install -e .
python examples/zerodivision.py
```

# License

See [LICENSE] file for details.