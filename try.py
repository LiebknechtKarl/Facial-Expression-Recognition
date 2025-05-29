import csv
from datetime import datetime
b = datetime.now().strftime('%Y%m%d%H%M%S')
with open('Epoch_train.csv', "a") as f:
    f.write(datetime.now().strftime('%Y%m%d%H%M%S') + '\n')

####################################################
