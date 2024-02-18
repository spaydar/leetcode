from collections import defaultdict
import heapq
from typing import List

class TwitterProcessOnWrite:

    def __init__(self) -> None:
        self.followee_dict = defaultdict(set)
        self.tweet_dict = defaultdict(list)
        self.news_feed_dict = defaultdict(list)
        self.time = 0

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        self.tweet_dict[user_id].append((self.time, tweet_id, user_id))
        self.news_feed_dict[user_id].append((self.time, tweet_id, user_id))
        for follower_id in self.followee_dict[user_id]:
            self.news_feed_dict[follower_id].append((self.time, tweet_id, user_id))
        self.time += 1

    def get_news_feed(self, user_id: int) -> List[int]:
        return [t[1] for t in self.news_feed_dict[user_id][-1:-11:-1]]

    def follow(self, follower_id: int, followee_id: int) -> None:
        if follower_id in self.followee_dict[followee_id] or follower_id == followee_id:
            return
        self.followee_dict[followee_id].add(follower_id)
        i = len(self.news_feed_dict[follower_id]) - 1
        for t in reversed(self.tweet_dict[followee_id]):
            while i > -1 and t[0] < self.news_feed_dict[follower_id][i][0]:
                i -= 1
            self.news_feed_dict[follower_id].insert(i + 1, t)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if follower_id in self.followee_dict[followee_id]:
            self.followee_dict[followee_id].remove(follower_id)
            self.news_feed_dict[follower_id] = [t for t in self.news_feed_dict[follower_id] if t[2] != followee_id]

class TwitterProcessOnRead:

    def __init__(self) -> None:
        self.follower_dict = defaultdict(set)
        self.tweet_dict = defaultdict(list)
        self.time = 0

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        self.tweet_dict[user_id].append((self.time, tweet_id))
        self.time -= 1

    def get_news_feed(self, user_id: int) -> List[int]:
        result, min_heap = [], []
        def heap_push_tweet(followee_id: int, idx: int):
            if followee_id in self.tweet_dict and idx < len(self.tweet_dict[followee_id]):
                heapq.heappush(min_heap, (*self.tweet_dict[followee_id][(-1 * idx) - 1], followee_id, idx))
        heap_push_tweet(user_id, 0)
        for followee_id in self.follower_dict[user_id]:
            heap_push_tweet(followee_id, 0)
        while len(result) < 10 and min_heap:
            _, tweet_id, followee_id, idx = heapq.heappop(min_heap)
            result.append(tweet_id)
            heap_push_tweet(followee_id, idx + 1)
        return result

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.follower_dict[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if followee_id in self.follower_dict[follower_id]:
            self.follower_dict[follower_id].remove(followee_id)
