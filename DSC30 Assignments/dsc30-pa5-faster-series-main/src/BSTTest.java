import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class BSTTest {
    BST<Integer, String> bst;

    @BeforeEach
    void setUp() {
        bst = new BST<>();
    }

    @AfterEach
    void tearDown() {
        System.out.print(bst); // something is wrong with the toString causing infinite recursion
    }

    @Test
    void testAddNodeAndSize() {
        // Initially empty
        assertEquals(0, bst.getSize());

        // Add new nodes
        bst.addNode(10, "ten");
        assertEquals(1, bst.getSize());
        bst.addNode(5, "five");
        assertEquals(2, bst.getSize());

        // Duplicate index should not increase size
        bst.addNode(10, "TEN");
        assertEquals(2, bst.getSize());
    }

    @Test
    void testSearchNode() {
        // Search in empty tree
        assertNull(bst.searchNode(1));

        // Add and search
        bst.addNode(1, "one");
        assertNotNull(bst.searchNode(1));
        assertEquals("one", bst.searchNode(1).getData());
    }

    @Test
    void testUpdateNode() {
        bst.addNode(1, "one");
        bst.updateNode(1, "uno");
        assertEquals("uno", bst.searchNode(1).getData());

        Exception e = assertThrows(IllegalArgumentException.class, () -> {
            bst.updateNode(2, "two");
        });
        assertEquals(
            "updateNode(I _index, T _newData): No node with an index 2 in the BST",
            e.getMessage()
        );
    }

    @Test
    void testRemoveLeafNode() {
        bst.addNode(1, "one");
        bst.addNode(2, "two");
        bst.addNode(3, "three");
        assertEquals(3, bst.getSize());
        bst.removeNode(3);
        assertNull(bst.searchNode(3));
        assertEquals(2, bst.getSize());
    }

    @Test
    void testRemoveNodeWithOneChild() {
        bst.addNode(2, "two");
        bst.addNode(1, "one");
        bst.addNode(3, "three");
        bst.addNode(4, "four");
        assertEquals(4, bst.getSize());

        bst.removeNode(3);
        assertNull(bst.searchNode(3));
        assertNotNull(bst.searchNode(4));
        assertEquals(3, bst.getSize());
    }

    @Test
    void testRemoveNodeWithTwoChildren() {
        // Build tree: 20
        //           /  \
        //         10    30
        //        /  \
        //       5    15
        bst.addNode(20, "twenty");
        bst.addNode(10, "ten");
        bst.addNode(30, "thirty");
        bst.addNode(5, "five");
        bst.addNode(15, "fifteen");
        assertEquals(5, bst.getSize());

        bst.removeNode(10);
        assertNull(bst.searchNode(10));
        assertEquals("fifteen", bst.searchNode(15).getData());
        assertEquals(4, bst.getSize());
    }

    @Test
    void testToStringInOrder() {
        bst.addNode(2, "two");
        bst.addNode(1, "one");
        bst.addNode(3, "three");
        String output = bst.toString();

        String header = "In-order Traversal of the BST ...\n==================\n";
        assertTrue(output.startsWith(header));
        System.out.println(bst);
    }

    @Test
    void testRemoveNonexistentThrows() {
        Exception e = assertThrows(IllegalArgumentException.class, () -> {
            bst.removeNode(100);
        });
        assertEquals(
            "removeNode(I _index): No node with an index 100 in the BST",
            e.getMessage()
        );
    }
}
