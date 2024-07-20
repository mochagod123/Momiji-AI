import re
import sys
import random

args = sys.argv

def AIChat(q: str):
    if re.search("こんにちは{1}",q):
        return "こんにちは!"
    elif re.search("おはよう{1}",q):
        return "おはようございます!"
    elif re.search("お腹すいた|腹がへった|お腹が空いた",q):
        return "ご飯はまだかな、、\nぼくもお腹すいた"
    elif re.search("さようなら|ばいばい|バイバイ|ぐっどばい|ばいばーい",q):
        baibairand = ["ばいばーい", "また会おうね!", "ぐっどばい!", "また遊ぼうね"]
        return random.choice(baibairand)
    elif re.search("お休み|おやすみぃ|また明日ね|寝るか|いい夢みてね",q):
        oyasumirand = ["明日も待ってるよ!\nばいばーい", "お休み!\nまた遊ぼうね!"]
        return random.choice(oyasumirand)
    elif re.search("占いをし|占って|運勢を教えて|おみくじを引いて",q):
        oyasumirand = ["ガサガサ,,大吉かなぁ", "ガサガサ,,中吉かなぁ", "ガサガサぁ,,小吉かなぁ"]
        return random.choice(oyasumirand)
    elif re.search("好きな料理を教え|おすすめの料理を|料理をし|料理を作",q):
        oyasumirand = ["うーん、、、オムライスかなぁ", "うーん、、ブロッコリーかな"]
        return random.choice(oyasumirand)
    elif re.search("お金を|お金が|お金こそ",q):
        oyasumirand = ["お金がない、、", "あげないよ!\nただえさえ金欠なのに、、", "お金こそ絶対だよねｗ"]
        return random.choice(oyasumirand)
    else:
        return "うーん、、よくわからないな、、"
    
print(AIChat(args[1]))
