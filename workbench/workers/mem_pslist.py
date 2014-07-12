
''' Memory Image PSList worker. This worker utilizes the Rekall Memory Forensic Framework.
    See Google Github: http://github.com/google/rekall
    All credit for good stuff goes to them, all credit for bad stuff goes to us. :)
'''
import os
import mem_base

class MemoryImagePSList(mem_base.MemoryImageBase):
    ''' This worker computes pslist-data for memory image files. '''
    dependencies = ['sample']

    def __init__(self):
        ''' Initialization '''
        super(MemoryImagePSList, self).__init__()
        self.set_plugin_name('pslist')

# Unit test: Create the class, the proper input and run the execute() method for a test
import pytest
@pytest.mark.xfail
def test():
    ''' mem_pslist.py: Test '''

    # This worker test requires a local server running
    import zerorpc
    c = zerorpc.Client(timeout=120)
    c.connect("tcp://127.0.0.1:4242")

    # Store the sample
    data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../data/memory_images/exemplar4.vmem')
    md5 = c.store_sample('exemplar4.vmem', open(data_path, 'rb').read(), 'mem')

    # Unit test stuff
    input_data = c.get_sample(md5)

    # Execute the worker (unit test)
    worker = MemoryImagePSList()
    output = worker.execute(input_data)
    print '\n<<< Unit Test >>>'
    import pprint
    pprint.pprint(output)
    assert 'Error' not in output

    # Execute the worker (server test)
    output = c.work_request('mem_pslist', md5)
    print '\n<<< Server Test >>>'
    import pprint
    pprint.pprint(output)
    assert 'Error' not in output


if __name__ == "__main__":
    test()
