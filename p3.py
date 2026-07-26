# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:10:51 2026

@author: Sthuthi Sheela
"""

import pandas as pd
data_list=[(1,'Apple','Red',2),(2,'Banana','Yellow',5),(3,'Carrot','Orange',3),
           (4,'Dragon fruit','Pink',2)]
dl=pd.DataFrame(data_list,columns=['item_no','fruit_name','color','quantity(kg)'])
print(dl)