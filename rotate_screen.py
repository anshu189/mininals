'''
Author: Anshu Saini
GitHub: https://github.com/anshu189
Mail: anshusaini189381@gmail.com
Requirements: rotatescreen (pip install rotatescreen)
Program: Screen Rotator
NOTE: Run on your own risk ;)

'''

import rotatescreen as r
from time import sleep as s
srn = r.get_primary_display()
for i in range(113):
    s(1)
    srn.rotate_to(i*90 % 360)
