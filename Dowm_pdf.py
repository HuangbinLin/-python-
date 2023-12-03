import urllib.request
from tqdm import tqdm
def download_pdf_with_urllib(url, save_path):
    try:
        urllib.request.urlretrieve(url, save_path)
        # print("文件下载成功。")
        return True
    except Exception as e:
        # print(url)
        return False


with open('example_error.txt', 'w',encoding='utf-8') as file:
    pass

file_path = 'example2022.txt'
total_lines = sum(1 for line in open(file_path, 'r', encoding='utf-8'))

with open('example_error.txt', 'a',encoding='utf-8') as file_error:
    with open(file_path, 'r',encoding='utf-8') as file:
        for i in tqdm(file, total=total_lines, desc='Processing lines'):
            url = i.split("*")[0]
            obj_index = i.split("*")[1]
            title = i.split("*")[2]
            save_path = "{}/{}.pdf".format(obj_index,title)
            res = download_pdf_with_urllib(url,save_path)
            if res == False:
                file_error.write(url)
                file_error.write("  ")
                file_error.write(str(obj_index))
                file_error.write("---")
                file_error.write(title)  
                file_error.write('\n')