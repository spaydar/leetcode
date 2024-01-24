from typing import List

def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    if end_word not in word_list:
        return 0
    from collections import defaultdict, deque
    adjacency_dict = defaultdict(list)
    for word in word_list:
        for i in range(len(word)):
            adjacency_dict[word[:i] + '*' + word[i + 1:]].append(word)
    visited = set([begin_word])
    q = deque([(begin_word, 1)])
    while q:
        word, ladder_len = q.popleft()
        if word == end_word:
            return ladder_len
        for i in range(len(word)):
            for adj_word in adjacency_dict[word[:i] + '*' + word[i + 1:]]:
                if adj_word not in visited:
                    visited.add(adj_word)
                    q.append((adj_word, ladder_len + 1))
    return 0
