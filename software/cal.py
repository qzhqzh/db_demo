# calculate length of nc_ran

import sys

nc_rna = sys.argv[1]
outfile = sys.argv[2]

with open(outfile, 'w', encoding='utf-8')as fh:
    fh.write(str(len(nc_rna)))
