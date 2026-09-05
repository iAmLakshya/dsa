class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += f"{len(word)}#{word}"
        return res

    def decode(self, s: str) -> List[str]:
        print(s, len(s))
        words = []
        i = 0
        while i < len(s):
            word_len_ptr = i
            while s[i] != "#":
                i += 1
            word_len = int(s[word_len_ptr:i])
            i += 1
            word = s[i : i + word_len]
            words.append(word)
            i += word_len
        return words
