// https://leetcode.com/problems/intersection-of-two-linked-lists/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *pA = headA;
        ListNode *pB = headB;
        if (pA == NULL || pB == NULL) return NULL;

        while (pA != pB) {
            pA = (pA == NULL) ? headB : pA->next;
            pB = (pB == NULL) ? headA : pB->next;
        }
        return pA;

    }
};
