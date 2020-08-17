'use strict';

/**
 * @param {number[]} height
 * @return {number}
 */
const maxArea = (height) => {
    let result = 0;

    for (let i = 0; i < height.length; i++) {
        for (let j = height.length - 1; j > 0; j--) {
            const width = j - i;
            const length = Math.min(height[i], height[j])
            const area = length * width;

            if (area > result) {
                result = area;
            }
        }
    }

    return result;
};

const height = [1, 8, 6, 2, 5, 4, 8, 3, 7];

console.log(maxArea(height));
