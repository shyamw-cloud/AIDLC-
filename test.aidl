// Test AIDL interface for AIDLC framework
package com.aidlc.framework;

// Simple test service interface
interface ITestService {
    // Returns a greeting message
    String getGreeting();
    
    // Echo service
    String echo(String message);
}
