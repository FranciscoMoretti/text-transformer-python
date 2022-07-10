# text-transformer-python
Powerful transformer for text files


# Setup
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pre-commit install
```


# Create code blocks
For the CPP Guidelines example from https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md

Using search and replace from VS Code
Replace the following regex
```
(\n(^    (.*)$\n)+)
```
using this repl
```sh
```cpp$1```
```

This illustrates the need of text processing files as a single string to be able to match a multiline regex.


## Improve regex to not parse
----------------
"""
> * `Expects`     // precondition assertion. Currently placed in function bodies. Later, should be moved to declarations.```cpp
>                 // `Expects(p)` terminates the program unless `p == true`
>                 // `Expects` is under control of some options (enforcement, error message, alternatives to terminate)
```
> * `Ensures`     // postcondition assertion. Currently placed in function bodies. Later, should be moved to declarations.

"""
-------
