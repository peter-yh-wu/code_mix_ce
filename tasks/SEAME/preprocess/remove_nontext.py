'''
Removes data samples without text

Peter Wu
peterw1@andrew.cmu.edu
'''

import os

def data_with_text(paths, ys):
    '''Returns data samples with text

    Assumes that strip() was applied to each y in ys
    '''
    new_paths = []
    new_ys = []
    for i, path in enumerate(paths):
        if len(ys[i]) > 0:
            new_paths.append(path)
            new_ys.append(ys[i])
    return new_paths, new_ys

TRAIN_PATHS_FILE = 'train_paths.txt'
DEV_PATHS_FILE = 'dev_paths.txt'
TEST_PATHS_FILE = 'test_paths.txt'
TRAIN_YS_FILE = 'train_ys.txt'
DEV_YS_FILE = 'dev_ys.txt'
TEST_YS_FILE = 'test_ys.txt'

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPLIT_DIR = os.path.join(parent_dir, 'split')
train_paths_path = os.path.join(SPLIT_DIR, TRAIN_PATHS_FILE)
dev_paths_path = os.path.join(SPLIT_DIR, DEV_PATHS_FILE)
test_paths_path = os.path.join(SPLIT_DIR, TEST_PATHS_FILE)
train_ys_path = os.path.join(SPLIT_DIR, TRAIN_YS_FILE)
dev_ys_path = os.path.join(SPLIT_DIR, DEV_YS_FILE)
test_ys_path = os.path.join(SPLIT_DIR, TEST_YS_FILE)

with open(train_paths_path, 'r') as inf:
    train_paths = inf.readlines()
train_paths = [f.strip() for f in train_paths]
with open(dev_paths_path, 'r') as inf:
    dev_paths = inf.readlines()
dev_paths = [f.strip() for f in dev_paths]
with open(test_paths_path, 'r') as inf:
    test_paths = inf.readlines()
test_paths = [f.strip() for f in test_paths]
with open(train_ys_path, 'r') as inf:
    train_ys = inf.readlines()
train_ys = [y.strip() for y in train_ys]
with open(dev_ys_path, 'r') as inf:
    dev_ys = inf.readlines()
dev_ys = [y.strip() for y in dev_ys]
with open(test_ys_path, 'r') as inf:
    test_ys = inf.readlines()
test_ys = [y.strip() for y in test_ys]

print('removing train files without text')
train_paths, new_train_ys = data_with_text(train_paths, train_ys)
print('removing dev files without text')
dev_paths, new_dev_ys = data_with_text(dev_paths, dev_ys)
print('removing test files without text')
test_paths, new_test_ys = data_with_text(test_paths, test_ys)

with open(train_paths_path, 'w+') as ouf:
    for path in train_paths:
        ouf.write('%s\n' % path)
with open(dev_paths_path, 'w+') as ouf:
    for path in dev_paths:
        ouf.write('%s\n' % path)
with open(test_paths_path, 'w+') as ouf:
    for path in test_paths:
        ouf.write('%s\n' % path)
with open(train_ys_path, 'w+') as ouf:
    for y in new_train_ys:
        ouf.write('%s\n' % y)
with open(dev_ys_path, 'w+') as ouf:
    for y in new_dev_ys:
        ouf.write('%s\n' % y)
with open(test_ys_path, 'w+') as ouf:
    for y in new_test_ys:
        ouf.write('%s\n' % y)