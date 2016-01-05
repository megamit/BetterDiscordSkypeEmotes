import json
import os, os.path
from PIL import Image
from collections import OrderedDict
import copy
##
##data = {}
##data["sprite20"] = {}
##data["sprite40"] = {}
##for root, _, files in os.walk("C:\\Dev\\Dump\\repo\\repository\\skype-emotes"):
##    for f in files:
##        fullpath = os.path.join(root, f)
##        if os.path.isfile(fullpath):
##            if fullpath[-4:]==".bmp":
##                i = Image.open(fullpath)
##                k= data["sprite"+str(i.width)]
##                k[":"+f[:-4]+":"] = {"url":"https://megamit.github.io/BetterDiscordSkypeEmotes/emotes/"+f,"type":"sprite"+str(i.width),"steps": int(i.height/i.width)}
##    file = open("skypeemotedata.json","w")
##    file.write(json.dumps(data,sort_keys=True,indent=4, separators=(',', ': ')));
##    file.close();
##
##keys = []
##dups = []
##def pair_decoder(args):
##    if len(args)!=3:
##        d = {}
##        for tup in args:
##            if tup[0] in keys:
##                dups.append(tup[0])
##            else:
##                keys.append(tup[0])
##            if not (tup[0] in d):
##                d[tup[0]] = {}
##            d[tup[0]][tup[1]["type"]]=tup[1]
##
##        return d
##    return todict(args)
##def todict(l):
##    newd = {}
##    for tup in l:
##        newd[tup[0]]=tup[1]
##    return newd
##s20 = []
##s40 = []
##with open("../data/skypeemotedata.json") as fin:
##    j = json.load(fin,object_pairs_hook=pair_decoder)
##    print(dups)
##    file = open("skypeemotedataV3.json","w")
##    file.write(json.dumps(j,sort_keys=True,indent=4, separators=(',', ': ')));
##    file.close();
##keys = []
##emos = {}
##dups = []
##def pair_decoder(args):
##    if len(args)!=3:
##        d = {}
##        for tup in args:
##            if tup[0] in keys:
##                dups.append(tup[0])
##            else:
##                keys.append(tup[0])
##            emos[tup[1]["url"][-8:-4]] = tup
##            if not (tup[0] in d):
##                d[tup[0]] = {}
##            d[tup[0]][tup[1]["type"]]=tup[1]
##            
##            
##                        
##                
##
##        return d
##    return todict(args)
##def todict(l):
##    newd = {}
##    for tup in l:
##        newd[tup[0]]=tup[1]
##    return newd
##s20 = []
##s40 = []
##def isnamed(ting):
##    return len(ting)!=6 or ting[0:1] != ":" or ting[-1:] != ":"
##with open("../data/skypeemotedata.json") as fin:
##    j = json.load(fin,object_pairs_hook=pair_decoder)
##    for key in list(j.keys()):
##        if isnamed(key) and len(j[key]) == 1:
##            val = {}
##            num = str((((int(list(j[key].values())[0]["url"][-8:-4])-7500)+200)%400)+7500)
##            try:
##                val = j.pop(":"+num+":")
##            except KeyError:
##                pass
##            if val:
##                j[key].update(val)
##                print("merged",num,"into",key)
##            else:
##                print("noaction")
##    #print(json.dumps(OrderedDict(sorted(emos.items(), key=lambda t: t[0])),sort_keys=True,indent=4, separators=(',', ': ')))
##    print(dups)
##    #print(json.dumps(j,sort_keys=True,indent=4, separators=(',', ': ')))
##    file = open("skypeemotedataV3.json","w")
##    file.write(json.dumps(j,sort_keys=True,indent=4, separators=(',', ': ')));
##    file.close();
##        
##def isnamed(ting):
##    return len(ting)!=6 or ting[0:1] != ":" or ting[-1:] != ":"
##with open("skypeemotedataV3.json") as fin:
##    j = json.load(fin)
##    for key in list(j.keys()):
##        if isnamed(key) and len(j[key]) == 1:
##            val = {}
##            num = str((((int(list(j[key].values())[0]["url"][-8:-4])-7500)+200)%400)+7500)
##            try:
##                val = j.pop(":"+num+":")
##            except KeyError:
##                pass
##            if val:
##                j[key].update(val)
##                print("merged",num,"into",key)
##            else:
##                print("noaction")
##    #print(json.dumps(OrderedDict(sorted(emos.items(), key=lambda t: t[0])),sort_keys=True,indent=4, separators=(',', ': ')))
##    #print(json.dumps(j,sort_keys=True,indent=4, separators=(',', ': ')))
##    file = open("skypeemotedataV3.5.json","w")
##    file.write(json.dumps(j,sort_keys=True,indent=4, separators=(',', ': ')));
##    file.close();
d = {}
with open("../data/skypeemotedata_v2.json") as fin:
    j = json.load(fin)
    for key in list(j.keys()):
        if "sprite20" in j[key]:
            d[key] = j[key]["sprite20"]
    file = open("../data/skypeemotedata.json","w")
    file.write(json.dumps(d,sort_keys=True,indent=4, separators=(',', ': ')));
    file.close();
