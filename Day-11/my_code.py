import requests
def add_new_user(user_dict,key,value):
    user_dict = {key: value}
    return user_dict
def update_dict(user_dict,key,value):
    user_dict[key]= value
    return user_dict
user_dict = {}
user_list =[]
j=1
repo_url="https://api.github.com/repos/iam-veeramalla/python-for-devops/pulls"
responses = requests.get(repo_url).json()
#print(type(responses))
for i in range(0,len(responses)):
    user_obj = responses[i]
    user = user_obj["user"]["login"]
    user_list.append(user)
    i = len(user_list)-2
while i>=0:
    if i == len(user_list)-2:
        if user_list[i] == user_list[i-1] or user_list[i] == user_list[i+1]:
            j+=1
            update_dict(user_dict,user_list[i],j)
        else:
            update_dict(user_dict,user_list[i],j)
            update_dict(user_dict,user_list[i+1],j)
    elif user_list[i] == user_list[i-1]:
        j+=1
        update_dict(user_dict,user_list[i],j)
    elif not(user_list[i] == user_list[i-1]) and not(user_list[i]==user_list[i+1]):
        j=1
        update_dict(user_dict,user_list[i],j)
    i-=1
    if i==0:
        j=1
        update_dict(user_dict,user_list[i],j)
# print(f"User list:{user_list}")
# print(f"User dict:{user_dict}")
i = len(user_list)-1
while i>=0:
    if i==0:
        print(f"User {user_list[i]} has {user_dict[user_list[i]]} pull history for the repo {repo_url}")
    elif user_list[i]==user_list[i-1]:
        k=1
    else: 
        print(f"User {user_list[i]} has {user_dict[user_list[i]]} pull history for the repo {repo_url}")
    i-=1