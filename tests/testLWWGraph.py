import unittest

from LWW.Graph import Graph as lww_graph


class Test_LWW_Graph(unittest.TestCase):
    def test_graph_init(self):
        '''
        test lww-graph init
        '''
        
        exception_received = False
        try:
            t = lww_graph()
        except:
            exception_received = True
        self.assertFalse(exception_received)
    def test_adding_vertex(self):
        '''
        test lww-graph addVertex
        '''
        t = lww_graph()
        t.addVertex(1)
    def test_removing_vertex(self):
        '''
        test lww-graph removeVertex
        '''
        t = lww_graph()
        t.addVertex(1)
    def test_vertex_exists(self):
        '''
        test lww-graph vertex exists
        '''
        t = lww_graph()
        vertex = 1
        t.addVertex(vertex)
        self.assertTrue(t.exists(vertex))
        t = lww_graph()
        self.assertFalse(t.exists(vertex))

    def test_adding_edge(self):
        '''
        test lww-graph addEdge
        '''
        t = lww_graph()
        t.addEdge(1,2)
    def test_removing_edge(self):
        '''
        test lww-graph removeEdge
        '''        
        g = lww_graph()
        try:
            g.removeEdge(1,2)
        except Exception as e:
            self.assertRaises(e, AssertionError)
    def test_merge(self):
        '''
        test graph merge
        '''
        g = lww_graph()
        z = lww_graph()
        g.merge(z)
    # def test_is_reachable()

if __name__ == '__main__':
    unittest.main()