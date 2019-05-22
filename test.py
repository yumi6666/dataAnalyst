# -*- coding: utf-8 -*-
import json

def resolveJson():
    file = open("newDataset.json", "r" ,encoding="UTF-8")
    new_dict = json.loads(str(file))
    # json.dump(new_dict,f)

resolveJson()