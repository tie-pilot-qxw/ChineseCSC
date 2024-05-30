
import random
import os
inputpath = './train_mix'
output = './train_mix'
output_name = ["train.txt","dev.txt","test.txt"]

files = ["ime","gam", "car", "nov", "enc", "new", "cot", "mec", "sig", "ec_law", "ec_med", "ec_odw"]
# for name in files:
#     filename = inputpath + '/' + name + '.txt'
#     with open(filename, 'r', encoding='utf-8') as file:
#         for line in file:
#             rand = random.random()
#             if rand < 0.6:
#                 each = output + '/' + name + '_' + output_name[0]
#                 out = output + '/' + output_name[0]
#             elif rand < 0.8:
#                 each = output + '/' + name + '_' + output_name[1]
#                 out = output + '/' + output_name[1]
#             else:
#                 each = output + '/' + name + '_' + output_name[2]
#                 out = output + '/' + output_name[2]
#             with open(out, 'a', encoding='utf-8') as o:
#                 o.write(line)
#             with open(each, 'a', encoding='utf-8') as e:
#                 e.write(line)
#             o.close()
    
for name in output_name:
    path = os.path.join(output, name)
    with open(path, 'w', encoding='utf-8') as out:
        for input in files:
            in_path = inputpath + '/' + input + '_' + name
            with open(in_path, 'r', encoding='utf-8') as file:
                for line in file:
                    out.write(line)