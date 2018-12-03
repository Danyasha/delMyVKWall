import vk_api

token = input("""
Get your token here \n
https://oauth.vk.com/authorize?client_id=6770459&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=wall&response_type=token&v=5.52\n
and put here\n""")
owner_id = input("Insert your user_ID:\n")
vk_session = vk_api.VkApi(login=None, password=None, token=token)
vk = vk_session.get_api()
posts = True
while (posts):
    posts = vk.wall.get(owner_id = owner_id, count = 100, filter = 'owner').get('items')
    posts_id = []
    for i in posts:
        posts_id.append(i.get('id'))
    for i in posts_id:
        vk.wall.delete(owner_id = owner_id, post_id = i)
print('Done')
input()