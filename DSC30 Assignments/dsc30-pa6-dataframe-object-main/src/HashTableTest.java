import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class HashTableTest {

    private HashTable<Integer> table;

    @Before
    public void setUp() {
        table = new HashTable<>();
    }

    @After
    public void tearDown() {
        System.out.println(table);
    }

    @Test
    public void testConstructor() {
        assertEquals(0, table.getSize());
        assertEquals(4, table.getCapacity());
    }

    @Test
    public void testInsertAndLookupBasic() {
        table.insert("a", 10);
        table.insert("b", 20);
        assertEquals(Integer.valueOf(10), table.lookup("a"));
        assertEquals(Integer.valueOf(20), table.lookup("b"));
        assertNull(table.lookup("z"));
    }

    @Test(expected = NullPointerException.class)
    public void testInsertNullKey() {
        table.insert(null, 1);
    }

    @Test(expected = NullPointerException.class)
    public void testInsertNullValue() {
        table.insert("a", null);
    }

    @Test(expected = NullPointerException.class)
    public void testLookupNullKey() {
        table.lookup(null);
    }

    @Test
    public void testInsertCollisionLinearProbing() {
        // Force collision by overriding getHashIndex if necessary during debugging
        table.insert("abc", 1);
        table.insert("acb", 2);
        assertEquals(Integer.valueOf(1), table.lookup("abc"));
        assertEquals(Integer.valueOf(2), table.lookup("acb"));
    }

    @Test
    public void testInsertUpdateValue() {
        table.insert("x", 100);
        int index1 = table.insert("x", 200);
        assertEquals(Integer.valueOf(200), table.lookup("x"));
        int index2 = table.getHashIndex("x");
        assertEquals(index1, index2);
    }

    @Test
    public void testLoadFactorResizeUp() {
        table.insert("a", 1);
        table.insert("b", 2);
        table.insert("c", 3);
        assertTrue(table.getCapacity() > 4); // Should have resized
    }

    @Test
    public void testDeleteAndBridge() {
        table.insert("a", 1);
        table.insert("b", 2);
        table.delete("a");
        assertNull(table.lookup("a"));
        assertEquals(Integer.valueOf(2), table.lookup("b"));
        assertEquals(1, table.getSize());
    }

    @Test(expected = NullPointerException.class)
    public void testDeleteNull() {
        table.delete(null);
    }

    @Test
    public void testLoadFactorResizeDown() {
        table.insert("a", 1);
        table.insert("b", 2);
        table.insert("c", 3);
        table.delete("a");
        table.delete("b");
        table.delete("c");
        assertTrue(table.getCapacity() >= 4); // Should not go below 4
    }

    @Test
    public void testToStringFormat() {
        table.insert("a", 10);
        table.insert("b", 20);
        String output = table.toString();
        System.out.println(output);
        assertTrue(output.contains("printing the hash table"));
        assertTrue(output.contains("key:\ta"));
        assertTrue(output.contains("data:\t10"));
    }

    @Test
    public void testKeyValueArrayCopies() {
        table.insert("a", 10);
        table.insert("b", 20);
        String[] keys = table.getKeyArray();
        Object[] values = table.getDataArray(); // ← Fix is here

        assertEquals(4, keys.length);
        assertEquals(4, values.length);
        assertEquals("a", keys[table.getHashIndex("a")]);
        assertEquals(10, values[table.getHashIndex("a")]); // or cast to Integer if needed
    }


    @Test
    public void testValidKeys() {
        table.insert("a", 1);
        table.insert("b", 2);
        table.delete("a");
        String[] validKeys = table.getValidKeys();
        assertEquals(1, validKeys.length);
        assertEquals("b", validKeys[0]);
    }
}

