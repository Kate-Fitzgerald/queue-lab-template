import queue

def test_queue():
    dmv = queue.Queue()
    dmv.push(1)
    dmv.push(2)
    dmv.push(3)
    dmv.pop()
    assert dmv.cards == [2,3]