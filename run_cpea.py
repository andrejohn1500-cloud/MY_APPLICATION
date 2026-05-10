import anthropic,json,os,time
client=anthropic.Anthropic(api_key="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")
OUT="app/src/main/assets/questions"
os.makedirs(OUT,exist_ok=True)
def gen(s,l):
    d="easy" if l<=3 else "medium" if l<=10 else "hard"
    p="Generate 15 MCQs for "+s+" Level "+str(l)+". Difficulty:"+d+". ONLY return a JSON array where each item has: question(string), options(array of 4 strings), correctIndex(integer 0-3). No other text."
    r=client.messages.create(model="claude-sonnet-4-6",max_tokens=2000,messages=[{"role":"user","content":p}])
    return json.loads(r.content[0].text)
for l in range(1,21):
    fp=OUT+"/cpea_social_studies_l"+str(l)+".json"
    if os.path.exists(fp):print("Skip",l);continue
    print("Gen",l)
    q=gen("CPEA Social Studies",l)
    json.dump(q,open(fp,"w"),indent=2)
    print("Done",l);time.sleep(2)
