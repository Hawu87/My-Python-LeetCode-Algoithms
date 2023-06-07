def addDigits(num):
        """
        :type num: int
        :rtype: int
        Return the sum of digits of num until you have a single digit
        >>> addDigits(38)
        2
        >>> addDigits(127)
        1
        """
        while num // 10 != 0:
            total = 0
            while num > 0:
                x = num % 10
                num //= 10
                total += x
            num = total
        return num
