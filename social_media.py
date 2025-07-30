from collections import Counter

posts = [
    {
        "id": 1,
        "user":"alice",
        "content":"Hello, world!",
        "likes":10,
        "tags":["python","programming","tech"],
    },
    {
        "id": 2,
        "user":"bob",
        "content":"Great Weather!",
        "likes":20,
        "tags":["weather","sunny","outdoor"],
    },
    {
        "id": 3,
        "user":"charlie",
        "content":"What a great cricket match!",
        "likes":30,
        "tags":["cricket","sports","match"],
    },
    {
        "id": 4,
        "user":"david",
        "content":"Enjoying the weekend!",
        "likes":40,
        "tags":["weekend","relax","fun"],
    },
    {
        "id": 5,
        "user":"emily",
        "content":"What a great code!",
        "likes":50,
        "tags":["code","python","tech"],
    },
    {
        "id": 6,
        "user":"frank",
        "content":"What a great code!",
        "likes":50,
        "tags":["work","python","tech"],
    }]

# tag_set = set()
# for post in posts:
#     tag_set.update(post["tags"])

# tag_map = {tag:0 for tag in tag_set}

# for post in posts:
#     for tag in post["tags"]:
#         tag_map[tag] += 1

# tag_map = sorted(tag_map.items(), key=lambda x: x[1], reverse=True)

# print(list(tag_map)[0:10:1][0][0])
    
tag_list = [tag for post in posts for tag in post["tags"]]

tag_counter = Counter(tag_list)

print(tag_counter.most_common(10))





