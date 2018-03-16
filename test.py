#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 20:45:43 2018

@author: spopoff
"""

#%%

import reportex,imp
import matplotlib.pyplot as plt
import numpy as np

imp.reload(reportex)



myreport = reportex.report('IL')

myreport.setTitle('My title', 'subtititle')
myreport.addText('Wouuuaaa, soo goood')

a = np.arange(10)
fig = plt.figure(figsize=(8, 6))
plt.plot(a,a**2)
myreport.addFig(fig)
#fig.savefig('destination_path.eps', format='eps', dpi=1000)

myreport.generatePDF('test')

