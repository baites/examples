class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letter_logs = []
        digit_logs = []

        while len(logs) > 0:
            log = logs.pop()
            fields = log.split()
            if fields[1].isnumeric():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        def letter_log_key(log):
            fields = log.split()
            return (fields[1:], fields[0])

        letter_logs.sort(key=letter_log_key)
        digit_logs.reverse()
        return letter_logs + digit_logs