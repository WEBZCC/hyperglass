#!/usr/bin/env python3
import os
import hyperglass
from hyperglass.hyperglass import app

application = app

hyperglass_root = os.path.dirname(hyperglass.__file__)
static = os.path.join(hyperglass_root, "static")

if __name__ == "__main__":
    application.renderCSS()
    application.run(static_folder=static)