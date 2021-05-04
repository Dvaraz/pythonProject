import json


if __name__ == '__main__':
    with open("worker.json", "r") as f:
        a = json.load(f)
        task_list = a[0]["task_list"]
        with open("worker.txt", "w") as f_new:
            for i in task_list:
                f_new.write(i['arguments'][0] + "\n")