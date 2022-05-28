#Assignment from ZuriI4G Fullstack scholarship Training

#Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
      if len(word) == len(anagram):
        if sorted(word) == sorted(anagram):
          return True
        else:
          return False
      else:
        return "Lengths not the same!"

find_anagram("heart", "earth")
find_anagram("hello", "check")
find_anagram("below", "elbow")