class Solution:
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):

        # Option 1: Buy type 1 and type 2 separately
        option1 = need1 * cost1 + need2 * cost2

        # Option 2: Buy common items for the minimum requirement
        common = min(need1, need2)

        option2 = common * costBoth

        if need1 > need2:
            option2 += (need1 - need2) * cost1
        else:
            option2 += (need2 - need1) * cost2

        # Option 3: Buy only type 3 items
        option3 = max(need1, need2) * costBoth

        return min(option1, option2, option3)
