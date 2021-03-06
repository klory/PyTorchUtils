
import argparse
import torch

# courtesy from https://discuss.pytorch.org/t/solved-keyerror-unexpected-key-module-encoder-embedding-weight-in-state-dict/1686/3
def clean_state_dict(state_dict):
    # create new OrderedDict that does not contain `module.`
    from collections import OrderedDict
    new_state_dict = OrderedDict()
    for k, v in state_dict.items():
        name = k[7:] if k[:min(6,len(k))] == 'module' else k # remove `module.`
        new_state_dict[name] = v
    return new_state_dict


def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

def requires_grad(model, flag=True):
    for p in model.parameters():
        p.requires_grad = flag

def clean_state_dict(state_dict):
    # create new OrderedDict that does not contain `module.`
    from collections import OrderedDict
    new_state_dict = OrderedDict()
    for k, v in state_dict.items():
        name = k[7:] if k[:min(6,len(k))] == 'module' else k # remove `module.`
        new_state_dict[name] = v
    return new_state_dict

def get_lr(optimizer):
    for param_group in optimizer.param_groups:
        return param_group['lr']

def sample_data(loader):
    """
    arguments:
        loader: torch.utils.data.DataLoader
    return:
        one batch of data
    usage:
        data = next(sample_data(loader))
    """
    while True:
        for batch in loader:
            yield batch

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


if __name__ == '__main__':
    pass