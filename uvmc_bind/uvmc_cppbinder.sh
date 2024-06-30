binder \
--root-module py_uvmc \
--prefix uvm_bindings \
--bind "" \
src/connect/sc/uvmc.hpp \
-- \
-std=c++11 \
-I../inc \
-Isrc/connect/sc \
-isysroot /Library/Developer/CommandLineTools/SDKs/MacOSX14.sdk