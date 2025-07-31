import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SeriesTest {

    Series<Double> s;

    @BeforeEach
    void setUp() {
        String[] rn = new String[] {"a", "b", "c"};
        Double[] data = new Double[] {1.0, 2.0, 3.0};
        s = new Series<Double>(rn, data);
        System.out.println(s);
    }

    @AfterEach
    void tearDown() {
        System.out.println(s);
        System.out.println("===========");
    }
    @Test
    void getDataTest() {
        String[] expected = {"1.0", "2.0", "3.0"};
        assertArrayEquals(expected, s.getData());
    }

    @Test
    void appendTest() {
        s.append("d", 4.0);
        assertEquals(4, s.getLength());
        assertArrayEquals(new String[] {"a", "b", "c", "d"}, s.getRowNames());
        assertArrayEquals(new String[] {"1.0", "2.0", "3.0", "4.0"}, s.getData());

        s.append("", 5.0);
        assertArrayEquals(new String[] {"a", "b", "c", "d", "4"}, s.getRowNames());
        assertArrayEquals(new String[] {"1.0", "2.0", "3.0", "4.0", "5.0"}, s.getData());

        s.append(null, 6.0);
        assertArrayEquals(new String[] {"a", "b", "c", "d", "4", "5"}, s.getRowNames());
        assertArrayEquals(new String[] {"1.0", "2.0", "3.0", "4.0", "5.0", "6.0"}, s.getData());
    }

    @Test
    void locTest() {
        assertThrows(NullPointerException.class, () -> s.loc((String) null));
        assertThrows(IllegalArgumentException.class, () -> s.loc(""));
        assertNull(s.loc("z"));
        assertEquals(2.0, s.loc("b"));
    }

    @Test
    void locArrayTest() {
        assertThrows(NullPointerException.class, () -> s.loc((String[]) null));
        assertThrows(IllegalArgumentException.class, () -> s.loc(new String[0]));

        assertArrayEquals(new Object[] {null, 2.0}, s.loc(new String[] {"z", "b"}));
        assertArrayEquals(new Object[] {3.0, 1.0}, s.loc(new String[] {"c", "a"}));
        assertArrayEquals(new Object[] {null, null}, s.loc(new String[] {"d", "e"}));
        assertArrayEquals(new Object[] {1.0}, s.loc(new String[] {"a"}));
    }

    @Test
    void ilocTest() {
        assertEquals(1.0, s.iloc(0));
        assertEquals(2.0, s.iloc(1));
        assertEquals(3.0, s.iloc(2));
        assertNull(s.iloc(3));  // out of bounds
    }

    @Test
    void dropTest() {
        assertThrows(NullPointerException.class, () -> s.drop(null));
        assertThrows(IllegalArgumentException.class, () -> s.drop(""));

        s.append("d", 4.0);

        assertFalse(s.drop("z"));
        assertEquals(4, s.getLength());

        assertTrue(s.drop("d"));
        assertEquals(3, s.getLength());
        assertArrayEquals(new String[] {"a", "b", "c"}, s.getRowNames());
        assertArrayEquals(new String[] {"1.0", "2.0", "3.0"}, s.getData());

        assertTrue(s.drop("b"));
        assertEquals(2, s.getLength());
        assertArrayEquals(new String[] {"a", "c"}, s.getRowNames());
        assertArrayEquals(new String[] {"1.0", "3.0"}, s.getData());

        assertTrue(s.drop("a"));
        assertEquals(1, s.getLength());
        assertArrayEquals(new String[] {"c"}, s.getRowNames());
        assertArrayEquals(new String[] {"3.0"}, s.getData());
    }

    @Test
    void fillNullTest() {
        assertThrows(IllegalArgumentException.class, () -> s.fillNull(null));

        s.append("d", null);
        s.append("e", 5.0);
        s.append("f", null);
        s.fillNull(10.0);

        assertArrayEquals(new String[] {"1.0", "2.0", "3.0", "10.0", "5.0", "10.0"}, s.getData());
    }
}
