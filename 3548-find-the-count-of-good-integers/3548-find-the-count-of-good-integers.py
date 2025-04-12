import math
from collections import Counter

class Solution:

    def _count_permutations(self, digit_counts, n):
        """ Calculates n! / (c0! * c1! * ... * c9!) using math.factorial """
        # Ensure all counts are non-negative integers
        if n < 0 or any(c < 0 for c in digit_counts.values()):
            return 0
            
        try:
            denom = 1
            for count in digit_counts.values():
                denom *= math.factorial(count)

            if denom == 0: return 0 # Avoid division by zero (e.g., if factorial overflows, though unlikely here)

            # Use integer division
            return math.factorial(n) // denom
        except (ValueError, OverflowError):
            # Handle potential errors if n or counts are too large for math.factorial
             # For typical constraints (n<=18), this should be fine.
            print(f"Warning: Factorial calculation error for n={n} or counts.")
            return 0


    def countGoodIntegers(self, n: int, k: int) -> int:
        """
        Counts n-digit numbers rearrangeable into a k-palindromic number.
        """
        # Length of the first half of the palindrome
        h = (n + 1) // 2

        # Range for the first half (prefix)
        # Smallest h-digit number (handle n=1 separately)
        start = 10**(h - 1) if n > 1 else 1
        # Smallest (h+1)-digit number gives the end boundary (exclusive)
        end = 10**h

        total_good_count = 0
        # Keep track of digit multisets already processed to avoid double counting
        processed_multisets = set()

        # 1. Generate palindromes from their first half
        for p_val in range(start, end):
            s_p = str(p_val) # String of the first half

            # Construct the full palindrome string
            if n % 2 == 1:
                # Odd n: Drop the middle digit for the reversed part
                s_rev_part = s_p[:-1][::-1]
            else:
                # Even n: Reverse the whole first half
                s_rev_part = s_p[::-1]
            palindrome_str = s_p + s_rev_part

            # 2. Check divisibility by k
            # Python handles large integers automatically
            palindrome_int = int(palindrome_str)
            if palindrome_int % k == 0:
                # This is a k-palindromic number

                # 3. Get the unique signature for this multiset of digits
                # Sorting digits makes the representation canonical
                multiset_key = tuple(sorted(palindrome_str))

                # 4. Calculate permutations only for new multisets
                if multiset_key not in processed_multisets:
                    processed_multisets.add(multiset_key)

                    # Count the frequency of each digit
                    digit_counts = Counter(palindrome_str) # e.g., {'2': 2, '0': 1}

                    # Calculate total permutations
                    total_perms = self._count_permutations(digit_counts, n)

                    # Calculate permutations starting with '0' (if '0' exists)
                    perms_leading_zero = 0
                    if '0' in digit_counts and digit_counts['0'] > 0:
                        # Create counts for remaining n-1 digits after fixing '0' first
                        temp_counts = digit_counts.copy()
                        temp_counts['0'] -= 1
                        # Remove '0' from counts if its count becomes 0
                        if temp_counts['0'] == 0:
                            del temp_counts['0']
                        perms_leading_zero = self._count_permutations(temp_counts, n - 1)

                    # Valid permutations (don't start with '0')
                    valid_perms = total_perms - perms_leading_zero
                    total_good_count += valid_perms # Add to the overall count

        return total_good_count
