#!/bin/bash

python << EOF > ./${2:-"nums"}.txt
import random
print "\n".join([str(random.randint(-1000,1000)) for _ in range($1)])
EOF
