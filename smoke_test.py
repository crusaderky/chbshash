"""Test import the library and print essential information"""

import platform
import sys

import correcthorse

print("Python interpreter:", sys.executable)
print("Python version    :", sys.version)
print("Platform          :", platform.platform())
print("Library path      :", correcthorse.__file__)
print("Library version   :", correcthorse.__version__)

assert correcthorse.hash(b"hello world") == "wob demonstrations rhinoderma behaviorist"
