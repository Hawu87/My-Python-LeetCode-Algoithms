class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #creating my hashmap to hold these a list as values
        my_dict = defaultdict(list) 

        #iterate through list
        for word in strs:
            #create a list made up of the number of appearances of the 26 lower case,
            #to hold as a key 
            count = [0] * 26

            #update the count array by adding one to the number of appearances of each letter
            for s in word:
                count[ord(s) - ord("a")] += 1

            #append the word to the right key, also append as tuple since lists cant be keys
            my_dict[tuple(count)].append(word)

        return my_dict.values()
