#!/usr/bin/env python3
from sort import *
from utility import *
from GUI import *


commands = [("Create", [1, 2, 3123, 4, 5, 612, 71231, 8, 9, 10, 11, 12, 13,
                            14, 15]),
            ("Compare", [0, 2, 1, 3123]),
            ("Result", [0, 2, "less than"])]

GUI(commands[::-1])
