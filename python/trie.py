class Trie:
    def __init__(self, char):
        self.char = char
        self.children = []
        self.word_finished = False

    def add(self, word: str):
        cur = self

        for char in word:
            is_in_children = False
            
            for child in cur.children:
                if char == child.char:
                    cur = child
                    is_in_children = True
                    break

            if not is_in_children:
                new_node = Trie(char)
                cur.children.append(new_node)
                cur = new_node

        cur.word_finished = True

    def find(self, word: str):
        cur = self
        r = []

        for char in word:
            is_in_children = False

            for child in cur.children:
                if char == child.char:
                    cur = child
                    is_in_children = True
                    break

            if not is_in_children:
                return r

        if cur.word_finished:
            r.append(word)

        r += self._find(cur, word)

        return r


    def _find(self, node, char):
        ans = []
        for child in node.children:
            if len(child.children) > 0 :
                ans += self._find(child, char + child.char)

            if child.word_finished:
                ans.append(char + child.char)

        return ans
