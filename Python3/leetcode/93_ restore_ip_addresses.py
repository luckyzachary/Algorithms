class Solution:

    def restore_ip_addresses(self, s):
        if len(s) < 4:
            return []

        result = []
        part = [0, 0, 0, 0]
        i1 = 1
        while i1 < 4 and i1 < len(s) - 2:
            part[0] = s[: i1]
            if not self.is_ip_part(part[0]):
                break
            i2 = i1 + 1
            while i2 - i1 < 4 and i2 < len(s) - 1:
                part[1] = s[i1: i2]
                if not self.is_ip_part(part[1]):
                    break
                i3 = i2 + 1
                while i3 - i2 < 4 and i3 < len(s):
                    part[2] = s[i2: i3]
                    if not self.is_ip_part(part[2]):
                        break
                    part[3] = s[i3:]
                    i3 += 1
                    if not self.is_ip_part(part[3]):
                        continue
                    result.append(".".join(part))
                i2 += 1
            i1 += 1
        return result

    @staticmethod
    def is_ip_part(s):
        if len(s) == 0:
            return False
        if s[0] == "0" and len(s) > 1:
            return False
        if int(s) > 255:
            return False
        return True


ro = Solution()
res = ro.restore_ip_addresses("172162541")
print(res)

