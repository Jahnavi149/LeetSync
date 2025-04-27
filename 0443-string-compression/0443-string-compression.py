class Solution:
    def compress(self, chars: List[str]) -> int:
        output = []
        curr = chars[0]
        count = 1
        for i in range(1, len(chars)):
            if chars[i] == curr:
                count += 1
                continue
            else:
                output.append(curr)
                if count == 1:
                    curr = chars[i]
                    count = 1
                    continue
                for x in str(count):
                    output.append(x)
                curr = chars[i]
                count = 1
        output.append(curr)
        if count == 1:
            pass
        else:
            for x in str(count):
                output.append(x)
        print(output)
        for i in range(len(output)):
            chars[i] = output[i]
        return len(output)
        