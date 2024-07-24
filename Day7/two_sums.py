def two_sum_linear(nums: list[int], target: int) -> list[int]:
        r = []
        compliment = dict()
        difference = [0]*len(nums)
        for i in range(len(nums)):
            d = target - nums[i]
            compliment[nums[i]] = [i, d]
            difference[i] = d
        for i in range(len(difference)):
            n = difference[i]
            if n in compliment:
                mapped_item = compliment[n]
                if mapped_item[0] != i:
                    r.append(i)
                    r.append(mapped_item[0])
                    
                    break
          
        return r


def two_sum_brute_force(nums: list[int], target: int) -> list[int]:
        r = []
        found = False
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    
                    r.append(i)
                    r.append(j)
                    found = True
                    break
                else:
                    pass
            if found:
                break
            
        return  r

nums = [2,7,11,15]

print(two_sum_brute_force(nums,9))
