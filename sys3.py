# Progress bar

import time

for i in range(50):
    time.sleep(0.1)
    print(f"{i} {'#'*i}{'.'*(50-i)}")