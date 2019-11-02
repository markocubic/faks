package com.mycompany.vjezba2;

public class MainClass {
    public static void main(String[] args) {

        String str = "Generate CRC32 Checksum For Byte Array Example";
        byte bytes[] = str.getBytes();
        Checksum checksum = new CRC32();
            
        checksum.update(bytes, 0, bytes.length);
        long lngChecksum = checksum.getValue();
        System.out.println("Test1:" + lngChecksum);
        
        checksum.reset();
        
        checksum.update(0);
        lngChecksum = checksum.getValue();
        System.out.println("Test2:" + lngChecksum);
        
        checksum.reset();
        
        checksum.update(bytes);
        lngChecksum = checksum.getValue();
        System.out.println("Test3:" + lngChecksum);
    }
}
