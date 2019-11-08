package com.mycompany.vjezba2;

import static org.testng.Assert.*;
import org.testng.annotations.AfterClass;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

/**
 *
 * @author Marko Ćubić
 */
public class CRC32NGTest {
    
    public CRC32NGTest() {
    }

    @BeforeClass
    public static void setUpClass() throws Exception {
    }

    @AfterClass
    public static void tearDownClass() throws Exception {
    }

    @BeforeMethod
    public void setUpMethod() throws Exception {
    }

    @AfterMethod
    public void tearDownMethod() throws Exception {
    }

    /**
     * Test of update method, of class CRC32.
     */
    @Test
    public void testUpdate_int() {
        System.out.println("update");
        int b = 0;
        CRC32 instance = new CRC32();
        instance.update(b);
   
        java.util.zip.CRC32 org = new java.util.zip.CRC32();
        org.update(b);
        
        assertEquals(instance.getValue(), org.getValue());
    }

    /**
     * Test of update method, of class CRC32.
     */
    @Test
    public void testUpdate_3args() {
        System.out.println("update");
        String str = "Generate CRC32 Checksum For Byte Array Example";
        byte bytes[] = str.getBytes();
        
        Checksum checksum = new CRC32();
        CRC32 instance = new CRC32();
        instance.update(bytes, 0, bytes.length);
        
        java.util.zip.Checksum checksum2 = new java.util.zip.CRC32();
        java.util.zip.CRC32 org = new java.util.zip.CRC32();
        org.update(bytes, 0, bytes.length);
        
        assertEquals(instance.getValue(), org.getValue());
    }

    /**
     * Test of update method, of class CRC32.
     */
    @Test
    public void testUpdate_byteArr() {
        System.out.println("update");
        String str = "Generate CRC32 Checksum For Byte Array Example";
        byte b[] = str.getBytes();
        CRC32 instance = new CRC32();
        instance.update(b);
        
        java.util.zip.CRC32 org = new java.util.zip.CRC32();
        org.update(b);
    }

    /**
     * Test of reset method, of class CRC32.
     */
    @Test
    public void testReset() {
        System.out.println("reset");
        CRC32 instance = new CRC32();
        instance.reset();
        
        java.util.zip.CRC32 org = new java.util.zip.CRC32();
        org.reset();
        
        assertEquals(instance.getValue(), org.getValue());
    }

    /**
     * Test of getValue method, of class CRC32.
     */
    @Test
    public void testGetValue() {
        System.out.println("getValue");
        CRC32 instance = new CRC32();
        long expResult = 0L;
        long result = instance.getValue();
        
        assertEquals(result, expResult);
    }
}
