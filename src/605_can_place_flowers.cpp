class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
                int size = flowerbed.size();
        for (int i = 0; i < size && n > 0; ++i) {
            if (flowerbed[i] == 0) {
                bool emptyLeft  = (i == 0      || flowerbed[i - 1] == 0);
                bool emptyRight = (i == size - 1 || flowerbed[i + 1] == 0);
                if (emptyLeft && emptyRight) {
                    flowerbed[i] = 1;  // plant here
                    --n;
                }
            }
        }
        return n <= 0;
    
    }
};
