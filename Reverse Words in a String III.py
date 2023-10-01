class Solution:
    def reverseWords(self, s: str) -> str:
        #hold the index of word size, and then do normal swaps in between that word
        i = j = 0
        output = ""
        while i < len(s):
            while j < len(s) and s[j] != " ":
                j += 1
            #get the string to reverse, j at white space
            output += s[i:j][::-1]
            # Add a space unless it's the last word
            if j < len(s):
                output += " "
            # Move to the next word
            j += 1
            i = j
        return output
                
        
            

            
        
