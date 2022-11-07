import pandas
from multiprocessing.dummy import Pool as ThreadPool
import os

DATA_LIST = []

def main():
    user_paths=["maildir/"+user for user in os.listdir("maildir")]
    for folder in user_paths:
        try:
            folder_names = [folder+"/"+sub_folder for sub_folder in os.listdir(folder)]
            pool = ThreadPool(100)
            pool.map(into_file,folder_names)
            pool.close()
            pool.join()
        except: 
            pass
    data = pandas.DataFrame(DATA_LIST)
    data.to_csv("the_enron_dataset_2.csv",index=False)

def into_file(path):
    global DATA_LIST
    try:
        item = {}
        files = [path+"/"+file for file in os.listdir(path)]
        for file_name in files:
            f = open(file_name,"r")
            data = f.readlines()
            f.close()
            msg_body = "".join(data).split("X-FileName: ")[-1]
            item["message"] = msg_body
            for data_lines in data:
                if "From: " in data_lines:
                    item["from"] = data_lines.split(" ")[-1]
                elif "To: " in data_lines:
                    item["to"] = data_lines.split(" ")[-1]
                elif "Subject: " in data_lines:
                    item["subject"] = data_lines.split(" ")[-1]
                else:
                    pass
            DATA_LIST.append(item)
        print("___ CURRENT STATUS : {} ___".format(len(DATA_LIST)))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
