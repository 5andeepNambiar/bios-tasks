## C programming:
      1.Learn about Caesar cipher and implement it in C.
      2.Learn about XOR, Implement Single Byte XOR encryption in C.


#### 1. Caesar's Cipher is basically to shift each letter of the plaintext by a fixed number down the alphabet to get the equivalent ciphertext.
Logic:<br/>
      (a) First,we accept a string, that is to be ciphered and a key from the user.The key shift each element a fixed number of times specified by the user.<br/>
      (b) Next,we initialise a for loop with basic conditions and assign each character of the string to a varible iteratively.<br/>
      (c) We then check if it is a lowercase or uppercase character using if else statements and add the ASCII values of the character of the string with the key and store it in the same varibale as above.<br/>
      (d) If ch is greater than the ascii value of z or Z( depends on whether character is uppercase or lowecase), then we subtract it from the ascii value of z or Z and add it with the ascii value of a or A and subract 1 from it.<br/>
      (e) Last, we assign the ciphered character back to the string variable and print the ciphered text outside after exiting from the loop.


#### 2. It is basically based on the bitwise XOR gate. If both the values or inputs are same, either both 0 or both 1, the output will be false(0) if not then True(1).In Single byte Xor encryption, the entire message is going to be xored with a single character. <br/>
Logic:<br/>
      (a) First, inside the main function, we accept a string and single byte character and pass that value to the function using function call statement.<br/>
      (b) We next define a function with two parameters, one for the string and the other for single byte character.<br/>
      (c) Next, we initialise a for loop and xor each character of the string with the key that is provided by the user untill the loop condition is false.<br/>
      (d) Last, we print the the encrypted string and teminate out of the loop.

