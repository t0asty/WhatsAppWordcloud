import re
import io
from collections import Counter
from wordcloud import WordCloud
import random
#from spacy.lang.de.stop_words import STOP_WORDS

STOP_WORDS = []
with open("../input/stop_words_german.txt", "r") as f:
    for word in f.readlines():
        STOP_WORDS.append(word.replace("\n",""))
STOP_WORDS = set(STOP_WORDS)

delete_datetime = re.compile("\[[0-9\.\,\: ]*\]")
# delete_names = re.compile(add usernames here....)
delete_endtoend = re.compile("Nachrichten und Anrufe sind Ende-zu-Ende-verschlüsselt. Niemand außerhalb dieses Chats kann sie lesen oder anhören, nicht einmal WhatsApp.", re.IGNORECASE)
delete_punctuation = re.compile("[^a-zäöüA-ZÄÖÜ]", re.IGNORECASE)

with io.open("../input/_chat.txt", "r") as f:
    chats = f.readlines()

def red_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    #print("hsl(0, 0%%, %d%%)" % random.randint(60, 100))
    #return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)
    return "rgb(%d, 0, 0)" % random.randint(100, 256)

res = []
for chat in chats:
    chat = delete_datetime.sub(' ',chat)
    # chat = delete_names.sub(' ',chat)
    chat = chat.replace("\n"," ")
    chat = delete_endtoend.sub(' ', chat)
    #chat = delete_punctuation.sub(' ', chat)
    chat = chat.replace("Audio weggelassen", " ")
    chat = chat.replace("Bild weggelassen", " ")
    chat = chat.lower()
    #chat = chat.format()
    chat = chat.split()
    res.append(chat)

print(res[:5])
final_li = []
print(len(res))
for x in res:
    final_li += x
#res = sum(res, start=[])
print(final_li[:5])
count = dict(Counter(final_li))
print(count)
print(list(STOP_WORDS))

font_path = "../input/OpenSansEmoji.ttf"

#count = {k: v for k, v in count.items() if k not in STOP_WORDS}

wc = WordCloud(font_path=font_path, background_color="black", max_words=200, random_state=5, color_func=red_color_func, width=1920, height=1080).generate_from_frequencies(count)
wc.to_file("../output/wordcloud.png")
