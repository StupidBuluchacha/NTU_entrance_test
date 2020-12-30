import pandas as pd
import os
import numpy as np
import torch
import torch.nn as  nn
import matplotlib.pyplot as plt
def data_loder(data_path,label_path=None):
    pd_data=pd.read_table(data_path)
    data=torch.from_numpy(pd_data.values)
    if label_path is not None:
        label=torch.from_numpy(pd.read_table(label_path).values)
        return data.type(torch.float32),label.type(torch.float32)
    return data.type(torch.float32)
class MLP(nn.Module):

    def __init__(self,n_features,n_hidden1,n_hidden2,n_output):
        super(MLP,self).__init__()
        self.hidden1=nn.Linear(n_features,n_hidden1)
        self.hidden2=nn.Linear(n_hidden1,n_hidden2)
        self.out=nn.Linear(n_hidden2,n_output)
    
    def forward(self,x):
        x=self.hidden1(x)
        x=nn.functional.relu(x)
        x=self.hidden2(x)
        x=nn.functional.relu(x)
        return self.out(x)

    

def main():
    train_path='data\\train_data.txt'
    train_label_path='data\\train_truth.txt'
    test_path='data\\test_data.txt'
    epochs=500
    lr=0.01
    X,Y=data_loder(train_path,train_label_path)
    net=MLP(3,4,4,1)
    loss_f=nn.MSELoss()
    opt=torch.optim.Adam(net.parameters(),lr=lr)
    ll=[]
    for i in range(epochs):
        y_pre=net(X)
        loss=loss_f(y_pre,Y)
        loss.backward()
        ll.append(loss)
        opt.step()
        opt.zero_grad()
    plt.plot(list(range(len(ll))),ll)
    plt.show()
    test_data=data_loder(test_path)
    test_pre=net(test_data)
    temp=test_pre.view(-1).detach().numpy().tolist()
    series=pd.Series({'y':temp})
    df = pd.DataFrame({'y': temp})
    df.to_csv("data\\test_predicted.txt",sep=",",columns=['y'],index=False,encoding='utf-8')
    print(test_pre)
main()

