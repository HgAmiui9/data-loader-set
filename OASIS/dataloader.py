from math import nan
import os
import torch
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
from torch.utils.data import Dataset, DataLoader

class OASISDataset(Dataset):

    def __init__(self, root, transform=None):
        self.transform = transform

        self.train_num, self.train_data, self.train_label, self.test_num, self.test_data, self.test_label  = self.loadCSV(root)

    def __len__(self):
        return 100

    def __getitem__(self, idx):
        if idx<len(self.data):
            data = self.data[idx]
            label = self.label[idx]
            return data, label

    def loadCSV(self, filename):

        pd_reader = pd.read_csv(filename)
        df = DataFrame(pd_reader)
        df = df.loc[:, ['ID', 'CDR']]

        # find all CDR not-non samples
        df = df[df['CDR'] <= 2]
        df.reset_index(drop=True, inplace=True)
        self.data = df
        label_dic = {0.0: 0, 0.5: 1, 1: 2, 2: 3}
        df['label'] = df['CDR'].map(label_dic)
        
        # divide label to traning set (80%) and test set(20%)
        label = np.asarray(df['label'])
        self.label

        label_ix = np.arange(len(label))
        np.random.shuffle(label_ix)
        label = label[label_ix]

        #devide dataset to traning set (80%) and test set(20%)
        df = df.loc[:, ['ID', 'CDR']]
        train_num = int(len(label) * 0.8)
        train_data = df.iloc[label_ix[:int(len(label)*0.8)]]
        train_labal = label[:int(len(label)*0.8)]

        test_num = int(len(label)) - train_num
        test_data = df.iloc[label_ix[int(len(label)*0.8):]]
        test_label = label[int(len(label)*0.8):]
        return train_num, train_data, train_labal, test_num, test_data, test_label

if __name__ == "__main__":
    filename = os.path.join(os.path.abspath(os.getcwd()), 'data-oasis1/oasis_cross-sectional.csv')
    oasis_data = OASISDataset(filename)
