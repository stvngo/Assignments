import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class SeriesV1Test {
    private SeriesV1<Double> s;

    @BeforeEach
    void setUp() {
        String[] rn = {"a", "b", "c"};
        Double[] data = {1.0, 2.0, 3.0};
        s = new SeriesV1<>(rn, data);
    }

    @Test
    void testGetters() {
        assertEquals(3, s.getLength());
        assertArrayEquals(new String[]{"a", "b", "c"}, s.getRowNames());
        assertArrayEquals(new String[]{"1.0", "2.0", "3.0"}, s.getData());
    }

    @Test
    void testAppend() {
        s.append("d", 4.0);
        assertEquals(4, s.getLength());
        assertArrayEquals(new String[]{"a", "b", "c", "d"}, s.getRowNames());
        assertArrayEquals(new String[]{"1.0", "2.0", "3.0", "4.0"}, s.getData());

        s.append("", 5.0);
        assertEquals(5, s.getLength());
        assertArrayEquals(new String[]{"a", "b", "c", "d", "4"}, s.getRowNames());
        assertArrayEquals(new String[]{"1.0", "2.0", "3.0", "4.0", "5.0"}, s.getData());

        s.append(null, 6.0);
        assertEquals(6, s.getLength());
        assertArrayEquals(new String[]{"a", "b", "c", "d", "4", "5"}, s.getRowNames());
        assertArrayEquals(new String[]{"1.0", "2.0", "3.0", "4.0", "5.0", "6.0"}, s.getData());
    }

    @Test
    void testLoc() {
        assertThrows(NullPointerException.class, () -> s.loc((String) null));
        assertThrows(IllegalArgumentException.class, () -> s.loc(""));
        assertNull(s.loc("z"));
        assertEquals(2.0, s.loc("b"));
    }

    @Test
    void testLocArray() {
        assertThrows(NullPointerException.class, () -> s.loc((String[]) null));
        assertThrows(IllegalArgumentException.class, () -> s.loc(new String[0]));

        Object[] out1 = s.loc(new String[]{"z", "b"});
        assertArrayEquals(new Object[]{null, 2.0}, out1);

        Object[] out2 = s.loc(new String[]{"c", "a"});
        assertArrayEquals(new Object[]{3.0, 1.0}, out2);

        Object[] out3 = s.loc(new String[]{"d", "e"});
        assertArrayEquals(new Object[]{null, null}, out3);

        Object[] out4 = s.loc(new String[]{"a"});
        assertArrayEquals(new Object[]{1.0}, out4);
    }

    @Test
    void testIloc() {
        assertEquals(1.0, s.iloc(0));
        assertEquals(2.0, s.iloc(1));
        assertEquals(3.0, s.iloc(2));
        assertNull(s.iloc(3));
    }

    @Test
    void testDrop() {
        assertThrows(NullPointerException.class, () -> s.drop(null));
        assertThrows(IllegalArgumentException.class, () -> s.drop(""));

        s.append("d", 4.0);
        assertFalse(s.drop("z"));
        assertEquals(4, s.getLength());

        assertTrue(s.drop("d"));
        assertEquals(3, s.getLength());
        assertArrayEquals(new String[]{"a", "b", "c"}, s.getRowNames());
        assertArrayEquals(new String[]{"1.0", "2.0", "3.0"}, s.getData());

        assertTrue(s.drop("b"));
        assertEquals(2, s.getLength());
        assertArrayEquals(new String[]{"a", "c"}, s.getRowNames());
    }

    @Test
    void testFillNull() {
        assertThrows(IllegalArgumentException.class, () -> s.fillNull(null));
        s.append("d", null);
        s.append("e", 5.0);
        s.append("f", null);
        s.fillNull(10.0);
        assertArrayEquals(new String[]{"1.0", "2.0", "3.0", "10.0", "5.0", "10.0"}, s.getData());
    }
}
