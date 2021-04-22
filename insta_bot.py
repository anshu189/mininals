'''
Author: Anshu Saini
GitHub: https://github.com/anshu189
Mail: anshusaini189381@gmail.com
Requirements: instabot (pip install instabot)
Program: Insta-Bot

'''

from instabot import Bot

bot = Bot()
bot.login(username="name", password="pass")

# # Upload pics
bot.upload_photo("smile.png", caption="Smile op")

# Follow
bot.follow("name2")

# # Send Message
bot.send_message("Hi", ["anshu_ck"])

# Followers name/info
followers = bot.get_user_followers("name3")
for follower in followers:
    info = bot.get_user_info(follower)
    print(info)

# Unfollow Everyone
bot.unfollow_everyone()
