from parse_llm_code import extract_first_code

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


class TestExtractFirstCode(unittest.TestCase):
    def test_length(self):
        result = extract_first_code(test_string)
        first_code_str = """print('first line')print('second line')"""
        self.assertEqual(
            result.length, 40, f"length test failed: expected {len(first_code_str)}"
        )

    def test_language(self):
        result = extract_first_code(test_string)
        self.assertEqual(
            result.language,
            "python",
            f"language test case failed: {result.language} != 'python' ",
        )

    def test_first_code_block_dic(self):
        result = extract_first_code(test_string)
        self.assertEqual(
            result.to_dict(),
            {
                "language": "python",
                "context": "print('first line')\nprint('second line')",
                "length": 40,
                "lines": 2,
                "include_try": False,
                "include_return": False,
            },
            "dict parse error",
        )


if __name__ == "__main__":
    unittest.main()
