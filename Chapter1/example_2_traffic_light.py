#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def coloring(G):
	color = 0
	groups = set()
	verts = vertices(G)
	while verts:
		new_group = set()
		for v in list(verts):
			if not_adjacent_with_set(v, newgroup, G):
				new_group.add(v)
				verts.remove(v)
		groups.add((color, new_group))
		colort += 1
	return groups