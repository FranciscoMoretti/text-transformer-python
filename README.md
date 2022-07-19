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


## Run Remark to add code fences
```
cd .sandbox/nodejs/
npm run format
```
Then copy the generated file
