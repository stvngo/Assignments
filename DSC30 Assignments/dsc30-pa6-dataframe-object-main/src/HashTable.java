public class HashTable <V> {

    private static final Object BRIDGE = new String("[BRIDGE]".toCharArray());
    private int size;
    private int capacity;
    private String[] keys;
    private V[] values;

    public HashTable() {
        this.size = 0;
        this.capacity = 4;
        this.keys = new String[this.capacity];
        this.values = (V[]) new Object[this.capacity];
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("printing the hash table ...\n==================\n");
        for (int i = 0; i < this.capacity; i++) { // use size or capacity?
            sb.append("index:\t").append(i).append(",\tkey:\t").append(this.keys[i])
                    .append(",\tdata:\t").append(this.values[i]).append("\n");
            // append converts to string before appending
        }
        return sb.toString();
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.capacity;
    }

    public String[] getKeyArray() {
        String[] copy = new String[this.capacity];
        for (int i = 0; i < this.capacity; i++) {
            copy[i] = this.keys[i];
        }
        return copy;
    }

    public V[] getDataArray() {
        V[] copy = (V[]) new Object[this.capacity];
        for (int i = 0; i < this.capacity; i++) {
            copy[i] = this.values[i];
        }
        return copy;
    }

    public String[] getValidKeys() {
        String[] copy = new String[this.size];
        int validIndex = 0;
        for (int i = 0; i < this.capacity; i++) {
            if (this.keys[i] != null && this.keys[i] != BRIDGE) {
                copy[validIndex] = new String(keys[i]);
                validIndex++;
            }
        }
        return copy;
    }

    public int getHashIndex(String k) { // k can only be lowercase letters
        int hashValue = 0;
        for (int i = 0; i < k.length(); i++) {
            int letter = k.charAt(i) - 96;
            hashValue += (hashValue * 27 + letter);
        }
        return hashValue % this.getCapacity();
    }

    public V lookup(String k) throws NullPointerException {
        if (k == null) {
            throw new NullPointerException("lookup(String key): key is null");
        }

        int index = this.getHashIndex(k);
        int originalIndex = index;

        while (index != originalIndex || keys[index] != null) {
            if (keys[index] == null) {
                return null;
            }
            if (keys[index].equals(k)) {
                return values[index];
            }
            index = (index + 1) % capacity;
            if (index == originalIndex) {
                break;
            }
        }

        return null;
    }

    public int insert(String k, V v) throws NullPointerException {
        if (k == null) {
            throw new NullPointerException("insert(String k, V v): k is null");
        }
        if (v == null) {
            throw new NullPointerException("insert(String k, V v): v is null");
        }
        
        int index = this.getHashIndex(k);
        int originalIndex = index;

        while (true) {
            if (keys[index] == null || keys[index] == BRIDGE) {
                // Empty or deleted spot found — insert new key
                keys[index] = k;
                values[index] = v;
                size++;

                // Resize check AFTER actual insert
                double loadFactor = (double) size / capacity;
                if (loadFactor >= 0.55) {
                    this.sizeUp();
                    return this.insert(k, v); // new index after rehash (it will skip this if-statement on the next call)
                }

                return index;
            } else if (keys[index].equals(k)) {
                // Key already exists — update and return index
                values[index] = v;
                return index;
            }

            index = (index + 1) % capacity;
            if (index == originalIndex) {
                break; // full cycle (shouldn't happen unless table is full)
            }
        }

        return -1;
    }

    private void sizeUp() {
        String[] oldKeys = this.keys;
        V[] oldValues = this.values;
        int oldCapacity = this.capacity;
        
        this.capacity *= 2;
        this.keys = new String[this.capacity];
        this.values = (V[]) new Object[this.capacity];
        this.size = 0;
        
        for (int i = 0; i < oldCapacity; i++) {
            if (oldKeys[i] != null && oldKeys[i] != BRIDGE) {
                insert(oldKeys[i], oldValues[i]);
            }
        }
    }

    private void sizeDown() {
        if (this.capacity <= 4) {
            return;
        }
        String[] oldKeys = this.keys;
        V[] oldValues = this.values;
        int oldCapacity = this.capacity;
        
        this.capacity /= 2;
        this.keys = new String[this.capacity];
        this.values = (V[]) new Object[this.capacity];
        this.size = 0;

        for (int i = 0; i < oldCapacity; i++) {
            if (oldKeys[i] != null && oldKeys[i] != BRIDGE) {
                insert(oldKeys[i], oldValues[i]);
            }
        }
    } 

    public int delete(String k) {
        if (k == null) {
            return getHashIndex(k);
        }

        int index = this.getHashIndex(k);
        int originalIndex = index;
        
        while (index != originalIndex || keys[index] != null) {
            if (keys[index] == null) {
                return getHashIndex(k);
            }
            if (keys[index].equals(k)) {
                keys[index] = (String) BRIDGE;
                values[index] = null;
                size--;
                
                // Check if we need to resize down
                double loadFactor = (double) size / capacity;
                if (loadFactor <= 0.3) {
                    sizeDown();
                }
                
                return index;
            }
            index = (index + 1) % capacity;
            if (index == originalIndex) {
                break;
            }
        }
        
        return getHashIndex(k);
    }
}
