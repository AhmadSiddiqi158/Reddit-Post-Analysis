import json,argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--coded_file', type=str, help="Name of coded tsv file")
parser.add_argument('-o', '--output_file', type=str, help='Name of the output json file')
args = parser.parse_args()

def main():

    df = pd.read_csv(args.coded_file, sep='\t')
    #print(df)
    c = df[df['coding'] == "c"]
    f = df[df['coding'] == "f"]
    r = df[df['coding'] == "r"]
    o = df[df['coding'] == "o"]
    
    dict = {
        "course-related": c.shape[0],
        "food-related": f.shape[0],
        "residence-related": r.shape[0],
        "other": o.shape[0]
    }
    json_object = json.dumps(dict, indent = 0)
    if(args.output_file == None):
        print(json_object)
    else:
        with open(args.output_file, "w") as outfile:
            outfile.write(json_object)

if __name__ == "__main__":
    main()