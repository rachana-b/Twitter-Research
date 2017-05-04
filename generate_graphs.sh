#!/bin/bash
python grapher.py log0.txt graph0.dot
python grapher.py log1.txt graph1.dot
python grapher.py log2.txt graph2.dot
python grapher.py log3.txt graph3.dot
python grapher.py log4.txt graph4.dot
python grapher.py log5.txt graph5.dot

dot -Tpdf graph0.dot -o graph0.pdf
dot -Tpdf graph1.dot -o graph1.pdf
dot -Tpdf graph2.dot -o graph2.pdf
dot -Tpdf graph3.dot -o graph3.pdf
dot -Tpdf graph4.dot -o graph4.pdf
dot -Tpdf graph5.dot -o graph5.pdf

