// https://leetcode.com/problems/filter-elements-from-array/

type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[] {
    let ans: number[] = [];
    let temp: boolean = false;

    for (let i = 0; i < arr.length; i++) {
        temp = fn(arr[i], i)

        if (temp) {
            ans.push(arr[i])
        }
    }

    return ans
};