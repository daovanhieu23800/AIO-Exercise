import torch


class Softmax(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        sum_exp = torch.sum(exp_x, dim=0)
        o = exp_x / sum_exp
        return o


class StableSoftmax(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = torch.max(x)
        x_sub = x - c
        exp_x = torch.exp(x_sub)
        sum_exp = torch.sum(exp_x, dim=0)
        o = exp_x / sum_exp
        return o


data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)

data = torch.Tensor([1, 2, 3])
stable_softmax = StableSoftmax()
output = stable_softmax(data)
print(output)
