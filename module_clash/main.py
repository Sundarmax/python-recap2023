from file1 import x
from file2 import x # file2 overrides file1 x value.

print(x) 

# proper example with namespace.

import file1
import file2

print(file1.x)
print(file2.x)