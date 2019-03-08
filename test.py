#!/usr/bin/env python3
import argparse
from sort import *
from utility import *
from GUI import *

commands = [("CreateList", [1, 2, 3123, 4, 5, 612, 71231, 8, 9, 10, 11, 12, 13, 14, 15]),
            ("Compare", [0, 2])]

GUI(commands[::-1])
