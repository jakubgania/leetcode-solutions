# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        temp_list = []
        
        for email in emails:
            if "+" in email:
                temp_list.append(
                    email[0:email.index("+")].replace(".", "") + email[email.index("@"):]
                )
            else:
                temp_list.append(
                    email[0:email.index("@")].replace(".", "") + email[email.index("@"):]
                )

        # for email in emails:
        #     item = email.split("@")
            
        #     if "+" in item[0]:
        #         item[0] = item[0][:item[0].index("+")]
            
        #     temp_list.append(item[0].replace(".", "") + "@" + item[1])

        return len(list(set(temp_list)))