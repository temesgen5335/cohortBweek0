import json
import argparse
import os
from os import path
import io
import shutil
import copy
from datetime import datetime
# from pick import pick
from time import sleep
import pandas as pd

# Create wrapper classes for using news_sdk in place of newser
class NewsDataLoader:
       def __init__(self):
        
        self.data = {}
        
        def load_data(self,path):
            if(path not in self.data):
                self.data[path] = pd.read_csv(path)
        return self.data[path]

   



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Export news history')
    parser.add_argument('--zip', help="Name of a zip file to import")
    args = parser.parse_args()