class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = "!?',;."
        for symbol in symbols:
            paragraph = paragraph.replace(symbol, ' ')
        counter = Counter([word.lower() for word in paragraph.split()])
        for word in banned:
            del counter[word]
        return counter.most_common(1)[0][0]