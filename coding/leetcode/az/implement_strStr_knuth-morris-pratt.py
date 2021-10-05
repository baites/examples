class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        def get_prefix_function(string):
            """Compute prefix function array.
               s[i] == lagest border for string[:i+1]
                                         i i+1
                # case 1: --x-- .... --x--x
                    s[i]  |---|      |---|
                          --x-- .... --x--x
                          |-|          |-|
                        border in 0..s[i]-1
                    so: s[i+1] = border of substring 0..s[i]-1
                                        i i+1
                # case 2: ----x .... ----x
                     s[i] |--|       |--|
                          ----x .... ----x
                          |---|      |---| s[i+1] = s[1] + 1

                # case 3: ----x .... ----y
                     s[i] |--|       |--|
                          ----x .... ----y
                          |              | s[i+1] = 0

            """
            size = len(string)
            border = 0
            prefix = [0]*size
            for i in range(1, size):
                while border > 0 and string[i] != string[border]:
                    border = prefix[border-1]
                if string[i] == string[border]:
                    border += 1
                else:
                    border = 0
                prefix[i] = border
            return prefix

        if len(haystack) < len(needle):
            return -1
        if len(needle) == 0:
            return 0

        composite = needle + '$' + haystack
        prefix = get_prefix_function(composite)
        n_size = len(needle)
        c_size = len(composite)

        for i in range(n_size+1, c_size):
            if prefix[i] == n_size:
                return i - 2 * n_size
        return -1