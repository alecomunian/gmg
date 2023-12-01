#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:This file:

    `2D_trend-artic.py`

:Purpose:

    Variogram along many directions of an artic subglacial topography.

:Usage:

    Explain here how to use it.

:Parameters:

:Version:

    Sun Nov  5 23:06:50 2023

:Authors:

    Alessandro Comunian

.. notes::
    See https://zenodo.org/records/5083715 for the complete dataset.
    Note that this script is very similar to `varioartic.py`.

.. warning::

.. limitations::
"""

import numpy as np
import matplotlib.pylab as pl
import gstools as gs 

# Load the data set
data = np.loadtxt("artic108.txt")

# Se the coordinates of the data-set, which is a square 200x200 cells domain.
# The side of the square cells is 500 m, but here for simplicity we will keep
# 1 m side cells.
x = np.arange(200)
y = np.arange(200)

# Define the bins to compute the variogram
bins = np.arange(0,100,2)

# Define some direction along which compute the variogram
# (the variable `ang_txt` is useful only for plotting purposes, and provides
#  the labels to each directional variogram.)
ang = [-np.pi/4, np.pi/4]
ang_txt = ["-$\\pi/4$", "$\\pi/4$"]

# Compute the experimental variogram
bin_center, gamma = gs.vario_estimate((x, y), data, bins, sampling_size=6000, 
                                      mesh_type="structured", angles=ang,
                                      bandwidth=4, angles_tol=np.pi/12)

#
# Plot
#
fig, ax = pl.subplots(1,2, figsize=((13,5)))
im = ax[0].imshow(data, origin="lower")
ax[0].set_xlabel("x")
ax[0].set_xlabel("y")
pl.colorbar(im)

for i, a in enumerate(ang):
    ax[1].plot(bin_center, gamma[i,:], "-o", label=ang_txt[i])
var = np.var(data[~np.isnan(data)])
ax[1].hlines(var, xmin=bin_center[0], xmax=bin_center[-1], ls="--", label="variance")
ax[1].legend()
ax[1].grid()
ax[1].set_xlabel("h [m]")
ax[1].set_ylabel("$\gamma(h)$ [m$^2$]")
pl.tight_layout()
pl.savefig("artic108_vario.png", dpi=400, transparent=True)
pl.show()


