from googletrans import Translator

translator = Translator()

with open("en.lproj/Localizable.strings", "r", encoding='utf-8') as f:
    lines = f.readlines()

with open("zh-Hans.lproj/Localizable.strings", "w", encoding='utf-8') as f:
    for line in lines:
        if '=' in line:
            key, value = line.split('=', 1)
            en_text = value.split('"')[1]  # 提取英文文本
            try:
                zh_text = translator.translate(en_text, src='en', dest='zh-cn').text
                f.write(f'{key.strip()} = "{zh_text}";\n')
            except:
                f.write(line)  # 翻译失败时保留原文
        else:
            f.write(line)