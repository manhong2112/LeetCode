/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* node(int val, struct ListNode* next);
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    if (l1 == NULL) {
        return l2;
    } else if (l2 == NULL) {
        return l1;
    } else {
        struct ListNode* l = node(l1->val + l2->val, addTwoNumbers(l1->next, l2->next));
        int next = l->val / 10;
        l->val %= 10;
        if(next != 0) {
            if(l->next != NULL) {
                l->next = addTwoNumbers(l->next, node(next, NULL));
            } else {
                l->next = node(next, NULL);
            }
        }
        return l;
    }
}

struct ListNode* node(int val, struct ListNode* next) {
    struct ListNode* l = malloc(sizeof(struct ListNode));
    l->val = val;
    l->next = next;
    return l;
}











