'use strict';

/**
 * @param {number[]} height
 * @return {number}
 */
const maxArea = (height) => {
    let largest = 0;

    let l = 0;
    let r = height.length - 1;

    while (l < r) {
        const width = r - l;
        const length = Math.min(height[l], height[r])
        const area = length * width;

        largest = Math.max(largest, area);

        height[l] < height[r] ? l++ : r--
    }

    return largest;
};

const height = [1, 8, 6, 2, 5, 4, 8, 3, 7];

console.log(maxArea(height));
