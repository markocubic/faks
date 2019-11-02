/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.vjezba2;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 *
 * @author LAPTOP
 */
public class CRC32Test {
    
    public CRC32Test() {
    }
    
    @BeforeAll
    public static void setUpClass() {
    }
    
    @AfterAll
    public static void tearDownClass() {
    }
    
    @BeforeEach
    public void setUp() {
    }
    
    @AfterEach
    public void tearDown() {
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
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of update method, of class CRC32.
     */
    @Test
    public void testUpdate_3args() {
        System.out.println("update");
        byte[] b = null;
        int off = 0;
        int len = 0;
        CRC32 instance = new CRC32();
        instance.update(b, off, len);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of update method, of class CRC32.
     */
    @Test
    public void testUpdate_byteArr() {
        System.out.println("update");
        byte[] b = null;
        CRC32 instance = new CRC32();
        instance.update(b);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of reset method, of class CRC32.
     */
    @Test
    public void testReset() {
        System.out.println("reset");
        CRC32 instance = new CRC32();
        instance.reset();
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
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
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }
    
}
