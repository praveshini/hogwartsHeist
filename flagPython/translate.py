# Parseltongue converter

# English to Parseltongue mapping
def convert(lang):
    if lang in ["parseltongue"]:
        text=input("Enter text: ")
        english_to_parseltongue = {
            'a': 'zhra',
            'b': 'kss',
            'c': 'tth',
            'd': 'dzh',
            'e': 'eezh',
            'f': 'ffth',
            'g': 'gzh',
            'h': 'hss',
            'i': 'iizh',
            'j': 'jzh',
            'k': 'kth',
            'l': 'lzh',
            'm': 'mzh',
            'n': 'nzh',
            'o': 'oozh',
            'p': 'pth',
            'q': 'qzh',
            'r': 'rzh',
            's': 'ssss',
            't': 'tth',
            'u': 'uuzh',
            'v': 'vzh',
            'w': 'wzh',
            'x': 'xzh',
            'y': 'yizh',
            'z': 'zzh',
            ' ': ' ',  # space remains unchanged
        }

        # Parseltongue to English mapping
        parseltongue_to_english = {}
        for k, v in english_to_parseltongue.items():
            for c in v:
                if c not in parseltongue_to_english:
                    parseltongue_to_english[c] = k

        def parseltongue(text):
            result = ""
            for c in text.lower():
                if c in english_to_parseltongue:
                    result += english_to_parseltongue[c]
                else:
                    result += c
            return result

        def english(text):
            result = ""
            i = 0
            while i < len(text):
                found = False
                for k, v in english_to_parseltongue.items():
                    if text[i:i+len(v)] == v:
                        result += k
                        i += len(v)
                        found = True
                        break
                if not found:
                    result += text[i]
                    i += 1
            return result
        print(english(text))
    else:
        print("No language detected")

# Test the converter
lang=input("Enter lang to be converted: ")
convert(lang)