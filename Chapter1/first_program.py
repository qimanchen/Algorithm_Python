#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Caculate sqrt for real number


def sqrt(x, e=0.01):
	y = 1.0
	while abs(y*y - x) > 1e-6:
		y = (y+x/y)/2
	return y
	
def sqrt_ite(x,  y=1.0, e=1e-6):
	if abs(y*y - x) < e:
		return y
	else:
		y = (y+x/y)/2
		return sqrt(x, y)
	
if __name__ == "__main__":
	x = 2
	y = sqrt_ite(x)
	
	print("The {} sqrt is {}".format(x, y))
	