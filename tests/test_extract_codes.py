from parse_llm_code import extract_code_blocks

import unittest

test_string = """
```python
print('first line')
print('second line')
```

```typescript
console.log('first line')
```
"""


class TestExtractCode(unittest.TestCase):
    def test_length(self):
        result = extract_code_blocks(test_string)
        self.assertEqual(result.length, 2, "length test failed: expected 2")

    def test_language(self):
        result = extract_code_blocks(test_string)
        self.assertEqual(
            result.code_list[0].language,
            "python",
            f"language test case failed: {result.code_list[0].language} != 'python' ",
        )
        self.assertEqual(
            result.code_list[1].language,
            "typescript",
            f"language test case failed: {result.code_list[1].language} != 'typescript' ",
        )

    def test_blocks_dic_list(self):
        result = extract_code_blocks(test_string)
        self.assertEqual(
            result.code_dict_list,
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
            ],
            "dict parse error",
        )


if __name__ == "__main__":
    unittest.main()
