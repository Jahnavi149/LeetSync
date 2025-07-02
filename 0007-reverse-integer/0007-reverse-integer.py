class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
        x = abs(x)
        x_str = str(x)
        r_x_str = x_str[::-1]
        reverse_int = int(r_x_str)
        if neg:
            reverse_int *= -1
        if reverse_int < -pow(2, 31) or reverse_int >= pow(2, 31):
            return 0
        return reverse_int

        