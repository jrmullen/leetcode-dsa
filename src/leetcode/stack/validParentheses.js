/**
 * @param {string} s
 * @return {boolean}
 */
const isValid = (s) => {
    let stack = [];

    for (let char of s) {
        let top = stack.length - 1;

        if (char === '(' || char === '[' || char === '{') {
            stack.push(char);
        } else if (stack.length !== 0 && char === ')' && stack[top] === '(') {
            stack.pop();
        } else if (stack.length !== 0 && char === ']' && stack[top] === '[') {
            stack.pop();
        } else if (stack.length !== 0 && char === '}' && stack[top] === '{') {
            stack.pop();
        } else {
            return false;
        }
    }

    return stack.length === 0;
};

let input = '()';

// Expected true
console.log(isValid(input));

// Expected true
input = '()[]{}';
console.log(isValid(input));

// Expected false
input = '(]';
console.log(isValid(input));

// Expected false
input = '([)]';
console.log(isValid(input));

// Expected true
input = '{[]}';
console.log(isValid(input));
