# Reddit-Post-Analysis

This project analyzes the main topics discussed on the /r/mcgill subreddit vs. the /r/concordia
subreddit.

1. collect_newest.py collects the 100 newest posts in the subreddit specified. It should run
as follows:

    ```python3 collect_newest.py -o <output_file> -s <<subreddit>subreddit>```
    
2. extract_to_tsv.py accepts one of the files you collected from Reddit and outputs a
random selection of posts from that file to a tsv (tab separated value) file. It should function like this:

    ```python3 extract_to_tsv.py -o <out_file> <json_file> <num_posts_to_output>```
    
    If <num_posts_to_output> is greater than the file length, then the script should just output all lines. If
    <num_posts_to_output> is less than the file length (which is likely the case), then it should randomly select
    num_posts_to_output (the parameter you passed to the script) of them and just output those.

The typology Categories:
* course-related (c)
* food-related (f)
* residence-related (r)
* other (o)

3. analyze.py outputs the number of each category that appears in your annotated
files. The script should run like this:

    ```python3 analyze.py -i <coded_file.tsv> [-o <output_file>]```

The “-o …” argument is optional. If omitted, the result will be printed to stdout. In either case, the output should be
written in JSON format like this:
```
{
 “course-related”: 70,
 “food-related”: 30,
 “residence-related”: 20,
 “other”: 80
}
