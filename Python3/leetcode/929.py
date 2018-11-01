#!/usr/bin/env python3

import pytest


class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        distinct_emails = []
        for email in emails:
            at_index = email.find("@")
            tail = email[at_index:]
            head = email[:at_index]
            plus = head.find("+")
            if plus != -1:
                head = head[:plus - 1]
            head = head.replace(".", "")
            dis_email = head + tail
            if dis_email not in distinct_emails:
                distinct_emails.append(dis_email)
        return len(distinct_emails)

def test_mytest():
    sol = Solution()
    assert sol.numUniqueEmails(["test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"]) == 2

test_mytest()
