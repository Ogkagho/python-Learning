# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:15:46 2024

@author: Edward kagho
"""

import matplotlib.pyplot as plt
import numpy as np

#plt.plot([1, 2, 3, 4], [1, 7, 3, 5])

principal = 10000
interest_rate = 0.05
years = 20
values = []
for i in range(years +1):
    values.append(principal)
    principal += principal*interest_rate

#plt.plot(values)
#plt.title('5% Growth, Compounded Annually')
#plt.xlabel('Years of compounding')
#plt.ylabel('Value of principal ($)')

plt.plot(values, '-k', linewidth = 30)
plt.title('5% Growth, Compounded Annually', 
          fontsize = 'xx-large')
plt.xlabel('Years of compounding', fontsize = 'x-small')
plt.ylabel('Value of principal ($)')

class Mortgage(object):
    
    def __init__(self, loan, annRate, months):
        self.loan = loan
        self.rate = annRate /12.0
        self.months = months
        self._paid = months
        self.outstanding = [loan]
        self.payment = find_payment(loan, self.rate, months)
        self.legend = None 
        
    def mak_payment(self):
        self._paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1]*self.rate 
        self.outstanding.append(self.outstanding[-1] - reduction)
    
    def get_total_paid(self):
        return sum(self._paid)
    
    def __str__(self):
        return self.legend 
    
    def plot_payments(self, style):
        plt.plot(self._paid[1:], style, label = self.legend)
    
    def plot_balance(self, style):
        plt.plot(self.outstanding, style, label = self.legend)
    
    def plot_tot_pd(self, style):
        tot_pd = [self._paid[0]]
        for i in range(1, len(self._paid)):
            tot_pd.append(tot_pd[-1] + self._paid[i])
        equity_acquired = np.array([self.loan]*len(self.outstanding))
        equity_acquired = equity_acquired-np.array(self.outstanding)
        net = np.array(tot_pd) - equity_acquired 
        plt.plot(net, style, labeel = self.legend)
