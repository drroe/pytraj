from __future__ import print_function
import unittest
from pytraj.base import *
from pytraj import allactions
from pytraj.cast_dataset import cast_dataset
from pytraj import adict
from pytraj.utils.check_and_assert import assert_almost_equal
from pytraj.decorators import no_test

farray = TrajReadOnly(top=Topology("./data/Tc5b.top"), 
                    filename='data/md1_prod.Tc5b.x', 
                    )
class TestRadgyr(unittest.TestCase):
    @no_test
    def test_0(self):
        dslist = DataSetList()
        act = adict['matrix']
        act.run(command="byres @CA", current_frame=farray, 
                current_top=farray.top, dslist=dslist)

        d1 = cast_dataset(dslist[0], dtype="matrix")
        print (d1.size)
        print (dir(d1))
        print (d1.n_cols, d1.n_rows)
        print (d1.dtype)
        print (d1.ndim)
        print (d1.kind)
        print (d1.data_format)
        # TODO : add assert to make sure reproducing cpptraj output

        for i in range(d1.size):
            print (d1[i])

        # another way
        d0 = adict['matrix']("byres @CA", farray, farray.top, quick_get=True)
        print (d0.size)
        print (dir(d0))
        print (d0.n_cols, d0.n_rows)
        print (d0.dtype)
        print (d0.ndim)
        print (d0.kind)
        print (d0.data_format)

        assert_almost_equal(d0, d1)
        d2 = adict['distance'](":2@CA :10@CA", farray, farray.top, quick_get=True)
        print (d2.dtype) 
        #assert d2[:] != d0[:]

    def test_1(self):
        dslist = DataSetList()
        act = adict['matrix']
        act.run(command="byres @CA", current_frame=farray, 
                current_top=farray.top, dslist=dslist)
        d0 = dslist[0]
        print (d0.alloc())
        print (d0.dtype)
        print (cast_dataset(d0, dtype=d0.dtype))
        print (dslist.get_dataset(0))

if __name__ == "__main__":
    unittest.main()