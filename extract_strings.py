import re
import os

def extract_strings(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # 忽略注释和 NSLog/CGLog 等调试语句
        strings = re.findall(r'(?<!Log\()"(?:\\.|[^\\"])*"', content)
        return [s for s in strings if not s.startswith('"\\"') and len(s) > 2]

with open("extracted_strings.txt", "w", encoding='utf-8') as out_file:
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".swift"):
                file_path = os.path.join(root, file)
                strings = extract_strings(file_path)
                if strings:
                    out_file.write("\n".join(strings) + "\n")