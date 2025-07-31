import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SeriesTestString {

    Series<String> s;

    @BeforeEach
    void setUp() {
        String[] rn = new String[] {"a", "b", "c"};
        String[] data = new String[] {"one", "two", "three"};
        s = new Series<String>(rn, data);
        System.out.println(s);
    }

    @AfterEach
    void tearDown() {
        System.out.println("===========");
    }

    @Test
    void getDataTest() {
        String[] expected = new String[] {"one", "two", "three"};
        assertArrayEquals(expected, s.getData());
    }

    @Test
    void appendTest() {
        String[] expectedRN1 = new String[] {"a", "b", "c", "d"};
        String[] expectedData1 = new String[] {"one", "two", "three", "four"};
        s.append("d", "four");
        assertEquals(4, s.getLength());
        assertArrayEquals(expectedRN1, s.getRowNames());
        assertArrayEquals(expectedData1, s.getData());

        String[] expectedRN2 = new String[] {"a", "b", "c", "d", "4"};
        String[] expectedData2 = new String[] {"one", "two", "three", "four", "five"};
        s.append("", "five");
        assertEquals(5, s.getLength());
        assertArrayEquals(expectedRN2, s.getRowNames());
        assertArrayEquals(expectedData2, s.getData());

        String[] expectedRN3 = new String[] {"a", "b", "c", "d", "4", "5"};
        String[] expectedData3 = new String[] {"one", "two", "three", "four", "five", "six"};
        s.append(null, "six");
        assertEquals(6, s.getLength());
        assertArrayEquals(expectedRN3, s.getRowNames());
        assertArrayEquals(expectedData3, s.getData());
    }

    @Test
    void locTest() {
        Exception e1 = assertThrows(NullPointerException.class, () -> {
            s.loc((String) null);
        });
        assertEquals("loc(String rn): rn can't be null", e1.getMessage());

        Exception e2 = assertThrows(IllegalArgumentException.class, () -> {
            s.loc("");
        });
        assertEquals("loc(String rn): rn can't be an empty string", e2.getMessage());

        assertNull(s.loc("z"));
        assertEquals("two", s.loc("b"));
    }

    @Test
    void locArrayTest() {
        Exception e1 = assertThrows(NullPointerException.class, () -> {
            s.loc((String[]) null);
        });
        assertEquals("loc(String[] rn): rn[] can't be null", e1.getMessage());

        String[] emptyArray = new String[0];
        Exception e2 = assertThrows(IllegalArgumentException.class, () -> {
            s.loc(emptyArray);
        });
        assertEquals("loc(String[] rn): rn[] can't be an empty array", e2.getMessage());

        Object[] expected1 = s.loc(new String[] {"z", "b"});
        Object[] expected2 = s.loc(new String[] {"c", "a"});
        Object[] expected3 = s.loc(new String[] {"d", "e"});
        Object[] expected4 = s.loc(new String[] {"a"});
        // case 1: input array has both valid and invalid rn
        assertArrayEquals(new Object[] {null, "two"}, expected1);
        assertEquals(2, expected1.length); // length of output array
        // case 2: input array has all valid rn
        assertArrayEquals(new Object[] {"three", "one"}, expected2);
        // case 3: input array has no valid rn
        assertArrayEquals(new Object[] {null, null}, expected3);
        // case 4: input array of one valid rn
        assertArrayEquals(new Object[] {"one"}, expected4);
        assertEquals(1, expected4.length);
    }

    @Test
    void ilocTest() {
        // case 1: index in bounds
        assertEquals("one", s.iloc(0));
        assertEquals("two", s.iloc(1));
        assertEquals("three", s.iloc(2));

        // case 2: index out of bounds
        assertNull(s.iloc(3));
    }

    @Test
    void dropTest() {
        Exception e1 = assertThrows(NullPointerException.class, () -> {
            s.drop((String) null);
        });
        assertEquals("drop(String rn): rn can't be null", e1.getMessage());

        Exception e2 = assertThrows(IllegalArgumentException.class, () -> {
            s.drop("");
        });
        assertEquals("drop(String rn): rn can't be an empty String", e2.getMessage());

        String[] expectedRN1 = new String[] {"a", "b", "c"};
        String[] expectedData1 = new String[] {"one", "two", "three"};
        String[] expectedRN2 = new String[] {"a", "c"};
        String[] expectedData2 = new String[] {"one", "three"};
        String[] expectedRN3 = new String[] {"c"};
        String[] expectedData3 = new String[] {"three"};
        s.append("d", "four");

        // case 1: rn cannot be found
        assertFalse(s.drop("z"));
        assertEquals(4, s.getLength());

        // case 2: drop from end
        assertTrue(s.drop("d"));
        assertEquals(3, s.getLength());
        assertArrayEquals(expectedRN1, s.getRowNames());
        assertArrayEquals(expectedData1, s.getData());

        // case 3: drop from middle
        assertTrue(s.drop("b"));
        assertEquals(2, s.getLength());
        assertArrayEquals(expectedRN2, s.getRowNames());
        assertArrayEquals(expectedData2, s.getData());

        // case 4: drop from front
        assertTrue(s.drop("a"));
        assertEquals(1, s.getLength());
        assertArrayEquals(expectedRN3, s.getRowNames());
        assertArrayEquals(expectedData3, s.getData());
    }

    @Test
    void fillNullTest() {
        Exception e = assertThrows(IllegalArgumentException.class, () -> {
            s.fillNull(null);
        });
        assertEquals("fillNull(T value): value can't be null", e.getMessage());
        s.append("d", null);
        s.append("e", "five");
        s.append("f", null);
        s.fillNull("HELLO WORLD");

        String[] expectedData = new String[] {"one", "two", "three", "HELLO WORLD", "five", "HELLO WORLD"};
        assertArrayEquals(expectedData, s.getData());
    }
}