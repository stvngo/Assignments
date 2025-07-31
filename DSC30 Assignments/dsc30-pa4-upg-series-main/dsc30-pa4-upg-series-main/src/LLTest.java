import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class LLTest {

    LL<Integer> list;

    @BeforeEach
    void setUp() {
        list = new LL<Integer>();
        list.appendNode("a", 1);
        list.appendNode("b", 2);
        list.appendNode("c", 3);
    }

    @AfterEach
    void tearDown() {
        System.out.println(list.toString());
        System.out.println("===========");
    }

    @Test
    void testAppendNodeAndGetArrays() {
        // initial state
        assertEquals(3, list.getLength());
        assertArrayEquals(new String[]{"1", "2", "3"}, list.getDataArray());
        assertArrayEquals(new String[]{"a", "b", "c"}, list.getIndexArray());

        // append normal node
        list.appendNode("d", 4);
        assertEquals(4, list.getLength());
        assertArrayEquals(new String[]{"1", "2", "3", "4"}, list.getDataArray());
        assertArrayEquals(new String[]{"a", "b", "c", "d"}, list.getIndexArray());

        // append with empty index -> default to numeric index
        list.appendNode("", 5);
        assertEquals(5, list.getLength());
        assertEquals("4", list.getIndexArray()[4]);
        assertEquals(5, Integer.parseInt(list.getDataArray()[4]));

        // append with null index -> default to numeric index
        list.appendNode(null, 6);
        assertEquals(6, list.getLength());
        assertEquals("5", list.getIndexArray()[5]);
        assertEquals(6, Integer.parseInt(list.getDataArray()[5]));
    }

    @Test
    void testSearchNode() {
        // existing nodes
        assertNotNull(list.searchNode("a"));
        assertEquals(1, list.searchNode("a").getData());
        assertNotNull(list.searchNode("b"));
        assertEquals(2, list.searchNode("b").getData());

        // non-existent
        assertNull(list.searchNode("z"));
    }

    @Test
    void testUpdateNode() {
        // update existing
        list.updateNode("b", 20);
        assertEquals(20, list.searchNode("b").getData());

        // update non-existent should throw
        Exception e = assertThrows(IllegalArgumentException.class, () -> {
            list.updateNode("z", 100);
        });
        assertEquals(
                "updateNode(String _index, T value): No node with an index z in the list",
                e.getMessage()
        );
    }

    @Test
    void testRemoveHeadNode() {
        list.removeNode("a");
        assertNull(list.searchNode("a"));
        assertEquals(2, list.getLength());
        assertNotNull(list.searchNode("b"));
        assertNotNull(list.searchNode("c"));
    }

    @Test
    void testRemoveMiddleNode() {
        list.removeNode("b");
        assertNull(list.searchNode("b"));
        assertEquals(2, list.getLength());
        assertNotNull(list.searchNode("a"));
        assertNotNull(list.searchNode("c"));
    }

    @Test
    void testRemoveTailNode() {
        list.removeNode("c");
        assertNull(list.searchNode("c"));
        assertEquals(2, list.getLength());
        assertNotNull(list.searchNode("a"));
        assertNotNull(list.searchNode("b"));
    }

    @Test
    void testRemoveSingleNode() {
        LL<Integer> singleList = new LL<>();
        singleList.appendNode("x", 10);
        singleList.removeNode("x");
        assertEquals(0, singleList.getLength());
        assertNull(singleList.searchNode("x"));
    }

}