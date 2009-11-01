from numpy.testing import *

from scikits.image import io
from scikits.image.io import plugin

from copy import copy

def read(fname, as_grey=False, dtype=None):
    assert fname == 'test.png'
    assert as_grey == True
    assert dtype == 'i4'

def save(fname, arr):
    assert fname == 'test.png'
    assert arr == [1, 2, 3]

def show(arr, plugin_arg=None):
    assert arr == [1, 2, 3]
    assert plugin_arg == (1, 2)

class TestPlugin:
    def setup(self):
        self.backup_plugin_store = copy(plugin.plugin_store)
        plugin.register('test', read=read, save=save, show=show)

    def test_read(self):
        io.imread('test.png', as_grey=True, dtype='i4', plugin='test')

    def test_save(self):
        io.imsave('test.png', [1, 2, 3], plugin='test')

    def test_show(self):
        io.imshow([1, 2, 3], plugin_arg=(1, 2), plugin='test')

    def teardown(self):
        plugin.plugin_store = self.backup_plugin_store


if __name__ == "__main__":
    run_module_suite()
