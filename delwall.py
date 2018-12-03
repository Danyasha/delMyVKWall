import vk_api

wallfilter = str(input("What to delete?\n1 for your only\n2 for non-your only\n3 for all\n"))
wallfilter = {'1':'owner', '2':'others', '3':'all'}.get(wallfilter)

token = input("""
Get your token here \n
https://oauth.vk.com/authorize?client_id=6770459&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=wall,photos&response_type=token&v=5.52\n
and put here\n""")
owner_id = input("Insert your user_ID:\n")
vk_session = vk_api.VkApi(login=None, password=None, token=token)
vk = vk_session.get_api()
posts = True
posts_id = []
photos_ids = []
while posts:
    posts = vk.wall.get(owner_id = owner_id, count = 100, filter = wallfilter).get('items')
    for i in posts:
        vk.wall.delete(owner_id = owner_id, post_id = i.get('id'))
print('Done')
input("press any key\n")