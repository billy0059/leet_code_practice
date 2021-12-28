'''
Found in internet, someone's phone-interview problem.
Given :
1. A list, 0 representing work day, 1 representing holiday.
2. A PTO count,
Return a number of longest continue-holidays.
'''
from typing import Optional
from typing import List

class Solution:

    def longestHoliday(self, holiday_list: List[int], pto: int) -> int:
        if len(holiday_list)==0:
            return 0
        start_index = 0
        end_index = 0
        logest_holiday = 0
        # Start to spend some PTOs on workdays!
        while end_index<len(holiday_list) and pto>0:
            if holiday_list[end_index] == 0: # means it is workday, we need take a pto
                pto -= 1
            end_index += 1
            logest_holiday = max(logest_holiday, end_index - start_index)

        # PTO is ran out and the work list is not yet finished, we need to shift the "window"
        while end_index<len(holiday_list):
            if holiday_list[end_index] == 1:
                end_index +=1
                logest_holiday = max(logest_holiday, end_index - start_index)
                continue
            elif holiday_list[start_index] == 1:
                start_index += 1
            else: # Previous pto change to the end_index position.
                start_index += 1
                end_index +=1
        return logest_holiday

def main():
    input = [1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0]
    pto = 10
    solution = Solution()
    print(solution.longestHoliday(input, pto))

if __name__ == '__main__':
    main()