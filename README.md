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

This illustrates the need of text processing files as a single string to be able to match a multiline regex. (TBD)

Then delete the `md` comments found with

```
<!--.*-->
```

Then replace the link in this format
```
<http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2015/n4477.pdf>
```

For this one
```
[Operator Dot (R2)](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2015/n4477.pdf)
```

## Replace images with references
Copy images to the public fonder and then replace the references.

To replace
```
![Normal parameter passing table](./param-passing-normal.png "Normal parameter passing")
```
with
```
![Normal parameter passing table](../public/param-passing-normal.png "Normal parameter passing")
```

and
```
![Advanced parameter passing table](./param-passing-advanced.png "Advanced parameter passing")
```
with
```
![Advanced parameter passing table](../public/param-passing-advanced.png "Advanced parameter passing")
```

## Remove another kind of comment
```
<< ??? We need another level of rule numbering ??? >>
```




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
