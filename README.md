![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FJKopiszka%2Fpyalgorithms%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.project.version&label=version&color=%2300aa00)
![Static Badge](https://img.shields.io/badge/license-GNU%20GPL%20v2.0-%2300aa00)

# PyAlgorithms #
**PyAlgorithms** is a simple Python package containing basic implementations of many algorithms.

>[!CAUTION]
>This package is still under development and does not provide stable release.

## Compatibility ##
- **Python 3** (recommended python version is 3.14+)
- **PIP 26.1**

## Installation ##
>[!NOTE]
>PyPI release is not supported at this moment.
### 1. Using github repository *(recommended)* ###
To install the package, use following 'PIP' package manager command:
```
pip install "git+https://github.com/JKopiszka/pyalgorithms"
```

### 2. Build the package by yourself ###
You can clone this repository and use it to build a package by yourself.
You need to execute:
```
git clone "https://github.com/JKopiszka/pyalgorithms.git"
```

and then in the directory of the project:

```
pip install .
```

## Usage ##

After package has been installed, you can import it to your code by using:
```python
import pyalgorithms
```
this will import every function as part of pyalgorithms "object".

## Documentation ##
- [API REFERENCE](./REFERENCE.md)