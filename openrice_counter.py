#%%
import json
FP = 'assets/scrapes/bs4/output_bs.jsonl'
#%%
# look
max_lines = 10
with open(FP,'r') as f:
    for i in range(max_lines):
        line = f.readline()
        d=json.loads(line)
        #print(d.keys())
        #print(d['url'])
        print(d['review'])
        print(len(d['review']))
        #review_chars = len(d['review'])

#%%

# count
total_review_chars = 0
with open(FP,'r') as f:
    keep_reading = True
    line_num = 0
    while keep_reading:
        line = f.readline()
        if line:
            try:
                d=json.loads(line)
            except Exception as e:
                print(line_num,line,e)
            review_chars = len(d['review'])
            total_review_chars += review_chars
            #print(line_num,review_chars)
        else:
            print(line_num,line)

        line_num += 1

print(f'total chars = {total_review_chars}')

#%%

#(base) alfred@net-g14:~/code$ sed -n '1230000,1231000{p}' OpenRice/openrice_recommendator/assets/scrapes/bs4/output_bs.jsonl
# wc -m  output_bs.jsonl # 657655730 output_bs.jsonl