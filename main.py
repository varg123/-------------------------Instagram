from instabot import Bot
import json
import re
import argparse
import os


# https://blog.jstassen.com/2016/03/code-regex-for-instagram-username-and-hashtags/
reg_exp_insta_frends = r"(?:@)([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)"
# https://stackoverflow.com/a/28840982
reg_exp_url = r"http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
CHECK_USER_EXIST = False
bot = Bot()
bot.login(
    username=os.getenv("LOGIN"),
    password=os.getenv("PASSWORD")
)


def get_parse_url():
    parser = argparse.ArgumentParser()
    parser.add_argument("post_url")
    post_url = parser.parse_args().post_url
    if not re.match(reg_exp_url, post_url):
        parser.error("url is incorrect")
    return post_url


def get_marked_friends(text_comment):
    return re.findall(reg_exp_insta_frends, text_comment)


def is_user_exist(text):
    return bool(bot.get_user_id_from_username(text))


def get_users_as_liked(media_id):
    return set(bot.get_media_likers(media_id))


def get_users_as_followed(media_id):
    media_info = bot.get_media_info(media_id)
    name_owner = media_info[0]['caption']['user']['username']
    return set(bot.get_user_followers(name_owner))


def get_users_marked_as_friends(comments):
    users = set()
    for comment in comments:
        marked_friends = get_marked_friends(comment['text'])
        for friend in marked_friends:
            if not CHECK_USER_EXIST or is_user_exist(friend):
                users.add(str(comment['user_id']))
                break
    return users


def main():
    media_url = get_parse_url()
    media_id = bot.get_media_id_from_link(media_url)
    comments = bot.get_media_comments_all(media_id)
    selected_users = get_users_marked_as_friends(comments)
    selected_users &= get_users_as_liked(media_id)
    selected_users = selected_users & get_users_as_followed(media_id)
    selected_users_names = set()
    for comment in comments:
        if str(comment['user_id']) in selected_users:
            selected_users_names.add(comment['user']['username'])
    count_selected_users = len(selected_users_names)
    print(f"Всего участников {count_selected_users}:")
    print(*tuple(selected_users_names), sep='\n')

if __name__ == '__main__':
    main()
