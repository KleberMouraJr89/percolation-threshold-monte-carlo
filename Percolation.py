import pandas as pd
import numpy as np
import random

from WeightedQuickUnionUF import soma, WeightedQuickUnion

class Percolation():
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.uf = WeightedQuickUnion(self.n * self.m)

        if n<=0 or m<=0:
            raise ValueError("IllegalArgumentException - `n` or `m` is equal or less than 0")
        
        self.matrix = np.ones((n,m))
    
    def __str__(self):
        return f"Matrix dimensions {self.n}x{self.m} \n {self.matrix}"

    
    def isOpen(self, r, c):
        
        if r < 0 or r >= self.n or c < 0 or c >= self.m:
            raise IndexError("Matrix query index error")
            
        matrix_query = self.matrix[r][c]
        
        return matrix_query==0
    
    def isFull(self, r, c):

        if r < 0 or r >= self.n or c < 0 or c >= self.m:
            raise IndexError("Matrix query index error")
            
        matrix_query = self.matrix[r][c]
        return matrix_query==1
    
    def numberOfOpenSites(self, sites=0):

        n_matrixOpen = np.sum(self.matrix==sites)
        return n_matrixOpen
    
    def _validate(self, row, col):
        if row < 0 or row >= self.n or col < 0 or col >= self.m:
            raise IndexError("index out of bounds")
    
    def newindex(self, r, c):
        index_= r * self.m + c

        return index_
    
    def connection_neighbors(self, r, c):

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # valida limites
            if 0 <= nr < self.n and 0 <= nc < self.m:

                # regra de negócio: só conecta se estiver "aberto"
                if self.matrix[nr][nc] == 0:
                    neighbor_index = self.newindex(nr, nc)
                    neighbors.append(neighbor_index)

        return neighbors
    
    def open(self, row, col):

        #validation
        self._validate(row, col)

        if self.matrix[row][col]==0:
            return

        self.matrix[row][col]=0
        neighbor_rootconn = self.connection_neighbors(row, col)
        index_ = self.newindex(row,col)

        if neighbor_rootconn==[]:
            return

        for i in neighbor_rootconn:

            matrix_index = self.uf.weightedqu(index_, i)

        return matrix_index