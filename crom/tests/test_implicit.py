import threading
from crom import implicit

def setup_module():
    implicit.initialize()

def teardown_module():
    implicit.clear()

def test_lookup_in_main():
    assert implicit.lookup is implicit.registry
    assert implicit.base_lookup is implicit.lookup
    
def test_lookup_in_thread_uses_default():
    log = []
    def f():
        log.append(implicit.lookup)
    
    thread = threading.Thread(target=f)
    thread.start()
    thread.join()
    assert len(log) == 1
    assert log[0] is implicit.registry

def test_changed_lookup_in_thread_doesnt_affect_main():
    # a different ILookup
    # (we don't actually fulfill the interface as that's not needed for
    # this test)
    different_lookup = object()

    log = []
    def f():
        implicit.lookup = different_lookup
        log.append(implicit.lookup)
    
    thread = threading.Thread(target=f)
    thread.start()
    thread.join()
    assert len(log) == 1
    assert log[0] is different_lookup
    assert implicit.lookup is implicit.registry
    assert implicit.lookup is implicit.base_lookup

def test_implicit_clear():
    implicit.clear()
    
    assert implicit.registry is None
    assert implicit.lookup is None
    assert implicit.base_lookup is None
    
    log = []
    def f():
        log.append(implicit.registry)
        log.append(implicit.lookup)
        log.append(implicit.base_lookup)
        
    thread = threading.Thread(target=f)
    thread.start()
    thread.join()
    assert log[0] is None
    assert log[1] is None
    assert log[2] is None
