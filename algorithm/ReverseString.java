package test;

public class ReverseString {
	
	/*
	 * This function uses a buffer array to reverse string 
	 */
	public String reverseString_1(String s) {
        if(s == null || s.length()<=1){
        	return s;
        }
        char[] buffer = s.toCharArray();
        char[] reverseBuffer = new char[s.length()];
        for(int i=0; i< s.length(); i++){
        	reverseBuffer[i]= buffer[s.length()-1-i];
        }
    	return new String(reverseBuffer);
    }
	
	/*
	 * This function uses Recursion method to reverse string 
	 */
	public String reverseString_2(String s) {
        if(s == null || s.length()<=1){
        	return s;
        }
    	return reverseString_2(s.substring(1))+s.charAt(0);
    }
	
	/*
	 * This function uses StringBuffer class to reverse string 
	 */
	public String reverseString_3(String s) {
        if(s == null || s.length()<=1){
        	return s;
        }
        StringBuffer sb = new StringBuffer(s);
        sb = sb.reverse();
    	return sb.toString();
    }
	
	public static void main(String[] args) {
		ReverseString rs = new ReverseString();
		String test = "hello";
		String result = rs.reverseString_3(test);
		System.out.println(result);
	}

}
