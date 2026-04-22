import pandas as pd
import numpy as np

def soma(a, b):
    return a + b

class WeightedQuickUnion():
    def __init__(self, N):
        self.n = N
        self.df = [i for i in range(N)]
        self.sz = [1] * N  # tamanho das árvores

    def __str__(self):
        return f"Tamanho {self.n} Array: {self.df}"

    def findroot(self, k):

        while k != self.df[k]:
            k = self.df[k]
        return k

    def connected(self, p, q):
        return self.findroot(p)==self.findroot(q)
    
    def weightedqu(self, p, q):

        root_p = self.findroot(p)
        root_q = self.findroot(q)
        
        if root_p == root_q:
            return self.df

        elif self.sz[root_p] < self.sz[root_q]:
            self.df[root_p] = root_q
            self.sz[root_q] += self.sz[root_p]
            
        else:
            self.df[root_q] = root_p
            self.sz[root_p] += self.sz[root_q]

        return self.df