import re

from typing import List


class CodeBlock:
    def __init__(self, language: str, context: str):
        self.language = language
        self.context = context
        self.length = len(context)
        self.lines = context.count("\n") + 1
        self.include_try = "try" in context
        self.include_return = "return" in context

    def to_dict(self) -> dict:
        return {
            "language": self.language,
            "context": self.context,
            "length": self.length,
            "lines": self.lines,
            "include_try": self.include_try,
            "include_return": self.include_return,
        }


class CodeBlocks:
    def __init__(self, code_list: List[CodeBlock]):
        self.length: int = len(code_list)
        self.code_list: List[CodeBlock] = code_list
        self.first: CodeBlock = code_list[0] if len(code_list) > 0 else None
        self.code_dict_list: List = [
            {
                "language": code.language,
                "context": code.context,
                "length": code.length,
                "lines": code.lines,
                "include_try": code.include_try,
                "include_return": code.include_return,
            }
            for code in code_list
        ]


def extract_code_blocks(md_string) -> CodeBlocks:
    code_blocks = []
    pattern = r"```(\w+)\n(.*?)\n```"
    matches = re.findall(pattern, md_string, re.DOTALL)
    for match in matches:
        language = match[0]
        context = match[1]
        code_blocks.append(CodeBlock(language, context))
    return CodeBlocks(code_blocks)


def extract_first_code(md_string) -> CodeBlock:
    code_blocks = []
    pattern = r"```(\w+)\n(.*?)\n```"
    matches = re.findall(pattern, md_string, re.DOTALL)
    for match in matches:
        language = match[0]
        context = match[1]
        code_blocks.append(CodeBlock(language, context))
    return CodeBlocks(code_blocks).first
