import json,argparse,csv,random

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output_file', type=str, help="Name of tsv output file", required=True)
parser.add_argument('json_file', type=str, help="Json file containing the posts")
parser.add_argument('num_posts_to_output', type=int, help="number of posts to write to out_file")
args = parser.parse_args()


def main():
    all_posts = []
    with open(args.json_file) as f1:
        for line in f1:
            content = []
            dict = json.loads(line)
            #print(dict["data"]["title"])
            content.append(dict["data"]["name"])
            content.append(dict["data"]["title"])
            all_posts.append(content)

    with open(args.output_file, 'w', newline='') as f1:
        tsv_out = csv.writer(f1, delimiter='\t')
        tsv_out.writerow(["Name", "title", "coding"])
        num = args.num_posts_to_output 
        if num < 100:
            all_posts = random.sample(all_posts, num)
        
        for post in all_posts:
            tsv_out.writerow(post)

if __name__ == "__main__":
    main() 