# config.py ---

import argparse
import getpass
import json
import os

class Config:
    def __init__(self):
        pass
args = Config()
args.w1bsroot = 'data/sets/wxbs-descriptors-benchmark/code/'
args.dataroot= 'data/sets/'
args.enable_logging = True
args.load_random_triplets = False
args.log_dir ='logs/'
args.model_dir = 'models/'
args.experiment_name = 'liberty_train/'
args.training_set = 'liberty'
args.loss = 'triplet_margin'
args.batch_reduce = 'min'
args.num_workers = 0
args.pin_memory= True
args.decor= False
args.anchorave = False
args.imageSize = 32
args.mean_image = 0.443728476019
args.std_image = 0.20197947209
args.resume = ''
args.start_epoch = 0
args.epochs = 10
args.anchorswap = True
args.batch_size = 1024
args.test_batch_size =1024
args.n_triplets = 50000
args.margin = 1.0
args.gor = False
args.freq = 10.0
args.alpha = 1.0
args.lr = 10.0
args.fliprot = True
args.augmentation = False
args.lr_decay = 1e-06
args.wd = 0.0001
args.optimizer = 'sgd'
args.no_cuda = False
args.gpu_id = '0'
args.seed = 0
args.log_interval = 10
args.cuda = True
args.dataset_names = ['liberty', 'notredame', 'yosemite']