import time
import requests

# Token और अन्य फ़ाइलों से डेटा पढ़ना
with open('Token.txt', 'r') as token_file:
    token = token_file.read().strip()

with open('Post link.txt', 'r') as post_file:
    post_link = post_file.read().strip()

with open('Time.txt', 'r') as time_file:
    delay_time = int(time_file.read().strip())

with open('Hatersname.txt', 'r') as haters_file:
    haters_comments = haters_file.readlines()

# Extract post ID from link
post_id = post_link.split('/')[-1].split('?')[0]

# Auto-comment script
for comment in haters_comments:
    url = f"https://graph.facebook.com/{post_id}/comments"
    payload = {
        'message': comment.strip(),
        'access_token': token
    }
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        print(f"Commented: {comment.strip()}")
    else:
        print(f"Failed to comment: {response.status_code}")
    
    time.sleep(delay_time)
