class Solution:
    def isPalindrome(number):

    # Determine whether an integer is a palindrome. An integer is a palindrome
    # when it reads the same backward as forward.
        temp_List = []
        list_copy = []
        for i in str(number):
            temp_List.append(i)
            list_copy.append(i)
        list_copy.reverse()
        print(temp_List)
        print(list_copy)
        if temp_List == list_copy:
            return True
        else:
            return False
    print(isPalindrome(121))

