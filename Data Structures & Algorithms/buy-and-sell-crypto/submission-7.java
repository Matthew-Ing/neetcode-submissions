class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int right = 1;
        int maxPrice = 0;

        while(right<prices.length){
            int currentPrice = prices[right] - prices[left];
            if (currentPrice<0){
                left = right;
            }
            maxPrice= Math.max(currentPrice, maxPrice);
            right++;
        }
        return maxPrice;
    }
}
