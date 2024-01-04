import os

os.makedirs("out",exist_ok=True)
f=open("out/out.md","w",encoding="utf-8")

dirs = [i for i in os.listdir() if not os.path.isfile(i) and i not in [".git","out",".github"]]
for chapter in dirs:
    f.write("# "+chapter+"\n\n")
    files=os.listdir(chapter)
    for file in files:
        f.write("## "+file.replace(".md","")+"\n")
        with open(chapter+"/"+file,"r",encoding="utf-8") as f2:
            f.write(f2.read()) 

f.close()