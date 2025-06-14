class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
      list = []
      min_length = min(len(word1),len(word2))# The loops that picks alternating characters can go up to minlength
      n = 0
      for n in range(min_length):
        list.append(word1[n])
        list.append(word2[n])
      if len(word1)>len(word2):
        list.append(word1[min_length:])
      else:
        list.append(word2[min_length:])
      return "".join(list)

      

       
    