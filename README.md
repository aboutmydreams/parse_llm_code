# parse_llm_code

This library serves the purpose of parsing code snippets from text, particularly helpful when dealing with outputs generated by large language models. Typically, such outputs include both code snippets and explanatory text. By using this library, one can effectively filter and extract the meaningful code portions, aiding in the extraction of useful and actionable code from generated responses.

## USECASE

### Extract first code block from answer

```python

from parse_llm_code import extract_first_code

test_string = """
this is llm answer example:

\```python
print('first line')
print('second line')
\```

 ```typescript
console.log('first line')
\```
"""

# Example of extracting the first code block
first_code = extract_first_code(test_string)
print(first_code.language)
print(first_code.context)
print(first_code.length)
print(first_code.lines)
print(first_code.to_dict())
```

Output

```python
python

print('first line')
print('second line')

40

2

{'language': 'python', 'context': "print('first line')\nprint('second line')", 'length': 40, 'lines': 2, 'include_try': False, 'include_return': False}
```

### Extract multi code blocks

```python
from parse_llm_code import extract_code_blocks

test_string = """
this is llm answer example:

\```python
print('first line')
print('second line')
\```

 ```typescript
console.log('first line')
\```
"""

# Example of extracting all code blocks
result = extract_code_blocks(test_string)
print(result.length)
print(result.code_list)
print(result.code_dict_list)
```

Output

```python
2

[<parse_llm_code.extract_code.CodeBlock object at 0x1049edac0>, <parse_llm_code.extract_code.CodeBlock object at 0x1049edfd0>]

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

## Run test

`python3 -m unittest discover -s tests`
