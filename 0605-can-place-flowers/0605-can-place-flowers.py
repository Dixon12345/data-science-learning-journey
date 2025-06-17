class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        padded_flowerbed = [0] + flowerbed +[0]
        for i in range(1,len(padded_flowerbed)-1):
            if padded_flowerbed[i] == 0 and padded_flowerbed[i-1]== 0 and padded_flowerbed[i+1] == 0:
                padded_flowerbed[i]=1
                n-=1
                if n<=0:
                    return True
        return n<=0
            

        