import json, requests,argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output_file', type=str, help="Name of output file")
parser.add_argument('-s', '--subreddit', type=str, help='Name of subreddit')
args = parser.parse_args()
################################################################################################
base_url = 'https://www.reddit.com/'
CLIENT_ID = 'Y5ALk8FdYMyFtbbD8IRaaA'
SECRECT = 'usTGSWwsaIGjQBjPU5hmq3WugeUEDg'
auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRECT)
data = {'grant_type': 'password', 'username': 'ahmadSiddiqi158', 'password': 'sIDA75060008#'}
res = requests.post(base_url + 'api/v1/access_token',
                  data = data,
                  headers = {'User-Agent': 'MyApi'},
		          auth=auth)
d = res.json()
token = 'bearer ' + d['access_token']
base_url = 'https://oauth.reddit.com'
headers = {'Authorization': token, 'User-Agent': 'APP-NAME by REDDIT-USERNAME'}
################################################################################################

def get_posts(subreddit):
    posts = []
    data = requests.get(f'https://oauth.reddit.com/{subreddit}/new', params={'limit':'100'}, headers=headers)
    posts.append(data.json()['data']['children'])
    return posts

def main():
    print(args.subreddit)
    print(args.output_file)
    
    posts = get_posts(args.subreddit)
    with open(args.output_file, "w") as f1:
        for dict in posts:
            for post in dict: 
                json.dump(post, f1)
                f1.write("\n")
    f1.close()



if __name__ == "__main__":
    main()