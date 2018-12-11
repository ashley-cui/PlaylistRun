# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 14:44:08 2018

@author: Jeffrey
"""
from flask import Flask, render_template

routeApp = Flask(__name__)
routeApp.secret_key = 'xuejf'
from routeApp import main