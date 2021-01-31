class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        returnNegative = False

        if x < 0:
            x *= -1
            returnNegative = True

        while (x > 0):
            remainder = x % 10

            if reverse > 214748364:
                reverse = 0
            else:
                reverse = (reverse * 10) + remainder

            x = x // 10
            
            #print(f"Remainder: {remainder}, Reverse: {reverse}, X: {x}")
        
        if returnNegative is True:
            return reverse*-1
        else:
            return reverse
