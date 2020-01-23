from client_vk import ClientGetID
from client_vk import ClientGetFriendsAges
from gists import Gist

debug = True
username = "Laptogol"

get_id = ClientGetID(username).execute()
friends_ages = ClientGetFriendsAges(get_id).execute()

if debug:
    print("ID: ", get_id)
    print("Ages: ", friends_ages)

title = "Ages of Users "
title_x = "Ages"
title_y = "Users"

mygist = Gist(friends_ages)
mygist.print_hist()
