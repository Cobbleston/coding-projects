/* Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
    Input: s = "cbaebabacd", p = "abc"
    Output: [0,6]
Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
    Input: s = "abab", p = "ab"
    Output: [0,1,2]
Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".

Constraints:
    1 <= s.length, p.length <= 3 * 104
    s and p consist of lowercase English letters. */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool isAnagram(string s1, string s2)
{
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());
    return (s1 == s2);
}

vector<int> findAnagrams(string s, string p)
{
    int lens = s.length();
    int lenp = p.length();
    vector<int> index;
    for (int i = 0; i < lens - lenp + 1; i++)
    {
        if (isAnagram(s.substr(i, lenp), p))
        {
            index.push_back(i);
        }
    }
    return index;
}

int main()
{
    vector<int> ciao = (findAnagrams("abab", "ab"));
    for (auto const &value : ciao)
    {
        cout << value << " ";
    }
    cout << endl;
    return 0;
}

/* O(n) solution:

class Solution
{
public:
    vector<int> findAnagrams(string s, string p)
    {
        int s_len = s.length();
        int p_len = p.length();

        if (s.size() < p.size())
            return {};

        vector<int> freq_p(26, 0);
        vector<int> window(26, 0);

        //first window
        for (int i = 0; i < p_len; i++)
        {
            freq_p[p[i] - 'a']++;
            window[s[i] - 'a']++;
        }

        vector<int> ans;
        if (freq_p == window)
            ans.push_back(0);

        for (int i = p_len; i < s_len; i++)
        {
            window[s[i - p_len] - 'a']--;
            window[s[i] - 'a']++;

            if (freq_p == window)
                ans.push_back(i - p_len + 1);
        }
        return ans;
    }
};*/