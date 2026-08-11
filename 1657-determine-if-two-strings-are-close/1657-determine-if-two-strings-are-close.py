class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # Step 1: Length same honi chahiye
        if len(word1) != len(word2):
            return False

        # Step 2: Frequency count karo
        count1 = {}
        count2 = {}

        for ch in word1:
            count1[ch] = count1.get(ch, 0) + 1

        for ch in word2:
            count2[ch] = count2.get(ch, 0) + 1

        # Step 3: Characters same hone chahiye
        if set(count1.keys()) != set(count2.keys()):
            return False

        # Step 4: Frequencies same honi chahiye
        freq1 = sorted(count1.values())
        freq2 = sorted(count2.values())

        if freq1 != freq2:
            return False

        return True