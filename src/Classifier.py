import jieba
from collections import Counter

class Classifier():
    def __init__(self):
        self.counter = Counter([])
        self.exclude = ("的", "了", "（", "）", "(",")", "'", "～", ",","着", "再", "Oh","啊","却", "在","是","就","都","而", "里", "~", "也", "那", "喔", "还", "会", "这", "有", "上", "很", "被", "给", "来", "为","只", "不","说", "啦", "让", "咪", "要")

    def update(self, sentences):
        seg_list = self.chinese_text_segementation(sentences)
        seg_list = list(filter(self.exclude_not_real_word, seg_list))
        self.counter.update(seg_list)

    def exclude_not_real_word(self, seg):
        if seg in self.exclude:
            return False
        else:
            return True

    def most_common(self, num):
        if len(self.counter) >= num:
            return self.counter.most_common(num)

    def chinese_text_segementation(self, sentences):
        seg_list = []
        for item in sentences:
            seg_list += jieba.cut(item, cut_all=False)
        return seg_list
