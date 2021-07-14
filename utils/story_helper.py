import re
import numpy as np
import tensorflow as tf
import os
import sys
from tf2gpt.model import GPT
from utils.story_util import Story,Stories
from utils.progress_bar import ProgressBar
from tensorflow.keras.utils import multi_gpu_model
import random
import textwrap
from utils.gpt2_tokenizer import GPT2Tokenizer
import tensorflow_hub as hub
cbpe = GPT2Tokenizer(
    'CPM-Generate/bpe_3w_new/vocab.json',
    'CPM-Generate/bpe_3w_new/merges.txt',
    model_file='CPM-Generate/bpe_3w_new/chinese_vocab.model')

gpt = None

def print_warp(instr):
    for i in textwrap.wrap(instr,width=50):
        print(i)

def initize(model_path="./tmp_weight"):
    global gpt
    gpt = hub.load(model_path)

def sample_gpt(tokenizer, gpt, sentence, number=1, length=20, p=0.9,k=40,temperature=0.4,penalize=0.85):
    inputs = tf.constant([tokenizer.encode(sentence)] * number, dtype=tf.int64)
    length = tf.constant(length, dtype=tf.int64)
    p = tf.constant(p, dtype=tf.float16)
    k = tf.constant(k, dtype=tf.int64)
    temperature = tf.constant(temperature, dtype=tf.float16)
    penalize = tf.constant(penalize, dtype=tf.float16)
    ret = gpt.signatures['serving_default'](
        inp=inputs, 
        length=length, 
        p=p,
        k=k,
        temperature=temperature,
        penalize=penalize)['output_0']
    return [
        tokenizer.decode(s[len(inputs[0]):]).replace(' ', '')
        for s in ret.numpy()
    ]

class Story():
    def __init__(self,beginning,story_max_len=200,context_len=12):
        self.story = [beginning]
        self.story_max_len = story_max_len
        self.context_len = context_len
        
    def response_quality_ok(self,response):
        if len(response) < 20:
            return False
        return True
    
    def action(self,action):
        action_str = "> 你" + action
        q = "".join(self.story[-self.context_len:]).replace("\n",'') + "\n" + action_str + "\n"
        q = q[-600:]
        self.story.append("你" + action)
        response = ""
        for i in range(3):
            response = sample_gpt(cbpe, gpt, q, 1, 150,p=0.9,k=16,temperature=1,penalize=0.75)[0]
            response = '。'.join(response.split("。")[:-1]) + "。"
            if(self.response_quality_ok(response) == True):
                break
            else:
                print_warp("Response quality check failed,generating another")
        
        #responsesp = response.split("。")
        #if(len(responsesp) > 2):
        #    response = ''.join(responsesp[:-1])
        #else:
        #    response = response.split(">")[0]
        #response = "。".join([:-1])
        #response = response.split(">")[0].strip()
        #response = "\n".join(response.split("\n")[:-1])
        self.story.append(response)
        
    def interactive(self):
        print_warp("\n".join(self.story))
        while True:
            action = input("> 你")
            self.action(action)
            print_warp(self.story[-1])