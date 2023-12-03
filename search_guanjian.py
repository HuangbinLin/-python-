import json
from Dowm import Dowm_data

def find_word(title, lists):
    # 转换输入单词和列表中的单词为小写，进行大小写不敏感的比较

    n = len(lists)
    for i in range(n):
        ns = len(lists[i])
        for k in range(ns):
            if lists[i][k] in title:
                return i + 1
    return None

word_lists = [
    ["Industrial Policy", "Shipping", "Aircraft", "Subsidy"],
    ["Market Integration", "Market Access"],
    ["Immigration", "Migration","Migrant"],
    ["Human Capital"],
    ["Comparative Advantage"],
    ["Manufacturing"],
    ["AI", "Artificial Intelligence"],
    ["Digital", "Platform", "E-commerce", "Electronic Commerce", "IT Technology", "IT"],
    ["Tax"],
    ["Innovation"],
    ["Patent"],
    ["Intellectual Property Protection","Intellectual Property"],
    ["Value Chain"],
    ["Servitization"]
]


with open('example1.txt', 'w',encoding='utf-8') as file:
    pass

with open('example1.txt', 'a',encoding='utf-8') as file:
    for page in range(1,25):
        file_path = "data\\2022\\page_{}_data.json".format(page)
        with open(file_path, 'r', encoding='utf-8') as file_data:
            data = json.load(file_data)
            for i in range(len(data["results"])):
                padded_i = str(i).zfill(2)
                title = data["results"][int(padded_i)]["title"]
                dowm_url = data["results"][int(padded_i)]["url"]
                # title_words = title.split()
                result = find_word(title,word_lists)
                if result != None:
                    file_index = result
                    obj_title = title
                    dowm_url = "https://www.nber.org/system/files/working_papers/" + dowm_url.split("/")[-1] +"/"+  dowm_url.split("/")[-1] + ".pdf"
                    file.write(dowm_url)
                    file.write("*")
                    file.write(str(file_index))
                    file.write("*")
                    file.write(obj_title)  
                    file.write('\n')