'use strict';

/**
 * @param {string} S
 * @return {string[]}
 */
const letterCasePermutation = (S) => {
    const result = [];

    if (!S) {
        return [];
    }

    const bfs = (left, rest, result) => {
        if (rest.length === 0) {
            result.push(left);
        } else {
            const ch = rest.charAt(0);

            // if the character is not a number, append upper & lower
            if (isNaN(ch)) {
                bfs(left + ch.toLowerCase(), rest.substr(1), result);
                bfs(left + ch.toUpperCase(), rest.substr(1), result);

            // if the character is a number, append it
            } else {
                bfs(left + ch, rest.substr(1), result);
            }
        }
    };

    bfs('', S, result);
    return result;
};

let S = 'a1b2';
console.log(letterCasePermutation(S));

S = '3z4'
console.log(letterCasePermutation(S));

S = '12345';
console.log(letterCasePermutation(S));
