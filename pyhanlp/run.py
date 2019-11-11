from pyhanlp import *

if __name__ == '__main__':
    tag = {}
    tag["主谓关系"] = "SBV"
    tag["动宾关系"] = "VOB"
    tag["介宾关系"] = "IOB"
    tag["前置宾语"] = "FOB"
    tag["兼语"] = "DBL"
    tag["定中关系"] = "ATT"
    tag["状中结构"] = "ADV"
    tag["动补关系"] = "CMP"
    tag["并列关系"] = "COO"
    tag["介宾关系"] = "POB"
    tag["介宾关系"] = "POB"
    tag["左附加关系"] = "LAD"
    tag["右附加关系"] = "RAD"
    tag["独立结构"] = "IS"
    tag["核心关系"] = "HED"
    tag["标点符号"] = "标点符号"

    sentence = "徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。"
    output = HanLP.parseDependency(sentence)
    print(output)
    result = []
    for word in output.iterator():
        data = {}
        data['dep'] = word.LEMMA
        data['gov'] = word.HEAD.LEMMA
        data['pos'] = tag[word.DEPREL]
        result.append(data)
    print(result)

    