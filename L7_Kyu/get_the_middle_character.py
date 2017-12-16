"""
https://www.codewars.com/kata/get-the-middle-character/train/python
You are going to be given a word. Your job is to return the middle character
of the word. If the word's length is odd, return the middle character.
If the word's length is even, return the middle 2 characters.

#Examples:

runBF("test\0") should return "es"

runBF("testing\0") should return "t"

runBF("middle\0") should return "dd"

runBF("A\0") should return "A"

#Input

A word (string) of length 0 < str < 200 For BF, all the input strings end
with "\0". You do not need to test for this. This is only here to tell you
that you do not need to worry about your solution timing out.

#Output

The middle character(s) of the word represented as a string.

Sample Tests:
Test.assert_equals(get_middle("test"),"es")
Test.assert_equals(get_middle("testing"),"t")
Test.assert_equals(get_middle("middle"),"dd")
Test.assert_equals(get_middle("A"),"A")
Test.assert_equals(get_middle("of"),"of")
"""


def get_middle(s):
    # your code here
    length = len(s)
    index = int(length/2)
    
    if length % 2 is not 0:
    	return(s[index])
    else:
    	return(s[index-1:index+1])


print(get_middle("test"))