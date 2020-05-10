#Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string ""

class Solution:
    def longestCommonPrefix(incoming_list):

        # print(incoming_list)
        # empty_default = "[empty......]"
        result_prefix = empty_default = "[empty......]"
        print(result_prefix)

        n = 0   #counter to get number of letters in each word
        for word in incoming_list:
            if result_prefix == empty_default:
                result_prefix = word
                continue
            for (c, c_res) in zip(word, result_prefix):
                if c != c_res:
                    if n == 0:
                        return ""
                    else:
                        break
                else:
                    n += 1
            result_prefix = result_prefix[0:n]
            #print("trim " + n)
            n = 0

        if result_prefix == empty_default:
            result_prefix = ""
        return result_prefix





