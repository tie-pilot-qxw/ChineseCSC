import os

files = ["ime","gam", "car", "nov", "enc", "new", "cot", "mec", "sig", "ec_law", "ec_med", "ec_odw"]
for name in files:
    output_dir = './lora_moe-mft/' + name
    command = "CUDA_VISIBLE_DEVICES=0 python run.py "
    command += "--output_dir " + output_dir + " "
    command += "--cache_dir ./cache "
    command += "--model_type relm "
    command += "--data_dir ./train_mix  "
    command += "--train_on " + name + "_train.txt "
    command += "--eval_on " + name + "_dev.txt "
    command += "--do_train --do_eval --train_batch_size 64 --eval_batch_size 64 --load_state_dict model/relm-m0.3.bin  "
    command += "--num_train_epochs 12 "
    command += "--mft"
    #command += "--save_steps 10 "
    #print("\"" + name +"\"" + " : " + "\"" + output_dir + "\",")
    #print(command)
    os.system(command)