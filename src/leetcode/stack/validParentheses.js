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
        }

        if (char === ')' && stack[top] === '(') {
            stack.pop();
        }

        if (char === ']' && stack[top] === '[') {
            stack.pop();
        }

        if (char === '}' && stack[top] === '{') {
            stack.pop();
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
