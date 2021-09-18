class Solution:
    def addBinary(self, a: str, b: str) -> str:

        def fun(da, db, c):
            if c==1:
                return da | db, 1-(da ^ db)
            return da & db, da ^ db

        result = ''

        c = 0
        ia = len(a)-1
        ib = len(b)-1

        # Loop over the digits
        while ia >= 0 or ib >= 0:
            da = 0 if ia < 0 else int(a[ia])
            db = 0 if ib < 0 else int(b[ib])

            # c: carry
            # v: digit value

            c, d = fun(da, db, c)
            result += str(d)

            ia -= 1 if ia >= 0 else 0
            ib -= 1 if ib >= 0 else 0

        # Apply any leftover carry
        if c > 0:
            c, d = fun(0, 0, c)
            result += str(d)

        return result[::-1]