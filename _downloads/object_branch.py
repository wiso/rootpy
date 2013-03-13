#!/usr/bin/env python
"""
===============
Object branches
===============

This simple example demonstrates how to define a TreeModel with a branch of type
std::vector<TLorentzVector>.
"""
print __doc__
import rootpy
rootpy.log.basic_config_colorized()
from rootpy.math.physics.vector import LorentzVector
from rootpy.tree import Tree, TreeModel
from rootpy.io import root_open as ropen
from rootpy.types import IntCol
from rootpy import stl
from random import gauss


f = ropen("test.root", "recreate")

# define the model
class Event(TreeModel):

    x = stl.vector('TLorentzVector')
    i = IntCol()

tree = Tree("test", model=Event)

# fill the tree
for i in xrange(100):
    tree.x.clear()
    for j in xrange(5):
        vect = LorentzVector(
                gauss(.5, 1.),
                gauss(.5, 1.),
                gauss(.5, 1.),
                gauss(.5, 1.))
        tree.x.push_back(vect)
    tree.i = i
    tree.fill()

tree.write()
f.close()
