import json
import sys


def extract_code_lines(text: str):
    """
    从 CST History Data Exchange Format V2 文本中提取所有 code 数组内容。
    文件开头可能包含非 JSON 标题，因此从第一个 '{' 开始解析。
    """
    start = text.find("{")
    if start == -1:
        raise ValueError("未找到 JSON 起始符号 '{'")

    data = json.loads(text[start:])
    lines = []

    for item in data.get("history", []):
        for code_line in item.get("code", []):
            # json.loads 已经将 \" 还原为 "，这里只去掉首尾多余空白
            lines.append(code_line.strip())

    return lines


def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else "CST History Data Exchange Format V2.txt"

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    result = "\n".join(extract_code_lines(text))
    print(result)


if __name__ == "__main__":
    main()