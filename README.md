# parse_llm_code

parse llm answer to code

## use case

Import and use it~

```python
from parse_llm_code.extract_code import extract_code_blocks

test_string = """
\```python
print('first line')
print('second line')
\```

 ```typescript
console.log('first line')
\```
"""

result = extract_code_blocks(test_string)
print(result.code_dict_list)
```

Output

```python
[
    {
        "language": "python",
        "context": "print('first line')\nprint('second line')",
        "length": 40,
        "lines": 2,
        "include_try": False,
        "include_return": False,
    },
    {
        "language": "typescript",
        "context": "console.log('first line')",
        "length": 25,
        "lines": 1,
        "include_try": False,
        "include_return": False,
    },
]
```

## run test

`python3 -m unittest discover -s tests`
