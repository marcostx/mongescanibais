#!/usr/bin/python

"""

//[]------------------------------------------------------------------------[]
//|                                                                          |
//|                      Problema dos Monges e Canibais                      |
//|                               Version 1.0                                |
//|                                                                          |
//|              Copyright 2015-2020, Marcos Vinicius Teixeira               |
//|                          All Rights Reserved.                            |
//|                                                                          |
//[]------------------------------------------------------------------------[]
//
//  OVERVIEW: mong_cabib.py
//  ========
//  Source file for solve the Cannibals and Missionaries Problem.				

#[ M, C, L]
# L = [-1,1] onde -1 lado direito e 1 lado esquerdo
# Estado inicial [3,3,-1]
# Estado final [0,0,1]

"""


class FIFOQueue():
    """A First-In-First-Out Queue."""
    def __init__(self):
        self.A = []; 
        self.start = 0
    def append(self, item):
        self.A.append(item)
    def __len__(self):
        return len(self.A) - self.start

    def pop(self):
        e = self.A[self.start]
        self.start += 1

        return e
    def __contains__(self, item):
        return item in self.A[self.start:]

def valid(state):
    ret  = True
    dm   = state[0]
    dc   = state[1]
    lado = state[2]
    em   = 3-dm
    ec   = 3-dc
    if dm < 0 or dm > 3: ret = False
    if dc < 0 or dc > 3:  ret = False
    if dc > dm and dm != 0: ret = False
    if ec > em and em != 0: ret = False
    return ret

def generate_children(state):
    lista = []
    monges    = state[0]
    canibais = state[1]
    lado     = state[2]
    inv_lado = lado*-1
    # Leva 1 canibal
    testado = [monges,canibais + lado,inv_lado]
    if valid(testado): lista.append(testado)

    # Leva 2 canibais
    testado = [monges,canibais + 2*lado,inv_lado]
    if valid(testado): lista.append(testado)

    # Leva 1 monge e 1 canibal
    testado = [monges+lado,canibais + lado,inv_lado]
    if valid(testado): lista.append(testado)

    # Leva 1 monge
    testado = [monges+lado,canibais,inv_lado]
    if valid(testado): lista.append(testado)

    # Leva 2 monges
    testado = [monges+2*lado,canibais,inv_lado]
    if valid(testado): lista.append(testado)

    return lista

def breadth_first_search(initial,final):
	initial_state = initial

	frontier = FIFOQueue()

	# explored list
	explored = []
	path = []
	father = dict()

	frontier.append(initial_state)

	while len(frontier) > 0:
		state = frontier.pop()

		if state == final:
			return state

		if state not in explored:
			explored.append(state)
			children = generate_children(state)
			for child in children:
				father['%d%d%d'%(child[0],child[1],child[2])] = state
				frontier.append(child)


if __name__ == '__main__':
	print breadth_first_search([3,3,-1],[0,0,1])
