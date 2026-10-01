import requests

response = requests.get('https://api.github.com/users/hiatus69')

if response.status_code == 200:
    user_data = response.json()

    print(f"Username: {user_data['login']}")
    print(f"Name: {user_data['name']}")
    print(f"Bio: {user_data['bio']}")
    print(f"Public: {user_data['public_repos']}")
    print(f"Followers: {user_data['followers']}")
    print(f"Following: {user_data['following']}")
else:
    print("Failed to retrieve data.")