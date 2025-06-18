class Solution:

    def reverseVowels(self, s: str) -> str:
        # Convert the string to a list of characters because strings are immutable in Python
        chars_list = list(s)

        # Initialize two pointers
        left = 0
        right = len(chars_list) - 1

        # Define the set of vowels for efficient lookup (O(1) on average)
        # Includes both lowercase and uppercase vowels
        vowels = set('aeiouAEIOU')

        # Continue the loop as long as the left pointer is to the left of the right pointer
        while left < right:
            # Move the left pointer forward until it finds a vowel
            # The 'left < right' check is crucial inside this inner loop
            # to prevent it from going out of bounds or crossing 'right'
            while left < right and chars_list[left] not in vowels:
                left += 1

            # Move the right pointer backward until it finds a vowel
            # The 'left < right' check is crucial inside this inner loop
            # to prevent it from going out of bounds or crossing 'left'
            while left < right and chars_list[right] not in vowels:
                right -= 1

            # After the inner loops, if left is still less than right,
            # it means both pointers have found a vowel (or met)
            if left < right:
                # Swap the characters at the left and right pointers
                # Python's elegant tuple assignment
                chars_list[left], chars_list[right] = chars_list[right], chars_list[left]
                
                # Move both pointers inwards after a successful swap
                left += 1
                right -= 1
        
        # Join the list of characters back into a string and return it
        return "".join(chars_list)


        