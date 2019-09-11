#导包
import yaml

def read_yaml(filename):
    with open("../data/"+ filename,"r",encoding="utf-8")as f:
        return yaml.load(f)


if __name__ == '__main__':
    # print(read_yaml().values())
    arrs = []
    for data in read_yaml("data.yaml").values():
       arrs.append((data.get("username"),data.get("password")))
    print(arrs)