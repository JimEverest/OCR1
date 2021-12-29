import random

test_ratio=0.1
lbl_file="datasets/labels.txt"
train_file='datasets/train.txt'
test_file='datasets/test.txt'

def getLineNum(lbl):
  file = open(lbl, "r")
  line_count = 0
  for line in file:
      if line != "\n":
          line_count += 1
  file.close()
  return(line_count)

n_lines=getLineNum(lbl_file)
n_val = int(n_lines*test_ratio)

# read everything in
lines = open(lbl_file).readlines()
# shuffle in random order
random.shuffle(lines)

# split array up and write out according to desired proportions
open(test_file, 'w').writelines(lines[:n_val])
open(train_file, 'w').writelines(lines[n_val:])

print("test data lines:", getLineNum(test_file))
print("terain data lines:", getLineNum(train_file))

