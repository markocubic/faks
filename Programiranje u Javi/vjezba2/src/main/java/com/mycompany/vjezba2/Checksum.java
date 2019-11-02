package com.mycompany.vjezba2;

public interface Checksum {
    public void update(int b);
    public void update(byte bytes[]);
    public void update(byte[] b, int off, int len);
    public long getValue();
    public void reset();
}
