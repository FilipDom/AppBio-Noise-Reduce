#! /usr/bin/env

import subprocess
import os

outputDir = os.path.abspath('./results/2012-12-21/noise_control')
subprocess.call(['python', './src/noiseReduceTest.py', outputDir])
