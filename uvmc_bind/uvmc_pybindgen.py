#! /usr/bin/env python

from pathlib import Path

import uvmc_bind.uvmc_pybindgen as uvmc_pybindgen
from uvmc_bind.uvmc_pybindgen import FileCodeSink
from pybindgen.castxmlparser import ModuleParser

def my_module_gen():
    module_parser = ModuleParser('svuvm')
    module = module_parser.parse(list(Path("src/connect/sc").glob("*.h")), include_paths=["inc/"])
    f = open("pyuvmc.cpp", "w")
    uvmc_pybindgen.write_preamble(FileCodeSink(f))
    module.generate(FileCodeSink(f))

if __name__ == '__main__':
    my_module_gen()