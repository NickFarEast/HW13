import json
from os.path import isfile

POST_PATH = "posts.json"


def get_posts_from_jason():
    if isfile(POST_PATH):
        with open(POST_PATH) as file:
            return json.load(file)
    else:
        print("Файл не найден")
        return {}


def get_post_by_tag(tag):
    posts = get_posts_from_jason()
    tag_match = f'#{tag}'
    posts_list = []

    for post in posts:
        if tag_match in post["content"]:
            posts_list.append(post)
    return posts_list



def get_all_tags_from_str(string):
    tags = set()

    for word in string.split(' '):
        if word.startswith('#'):
            tags.add(word[1:])

    return tags


def get_all_tags_from_posts():
    posts = get_posts_from_jason()
    tags = set()

    for post in posts:
        post_content = post.get('content')
        tag_in_posts = get_all_tags_from_str(post_content)
        tags = tags.union(tag_in_posts)

    return tags


