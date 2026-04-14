class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        // Define the mapping of closing to opening brackets
        const dictionary = {")": "(", "]": "[", "}": "{"};
        const stack = [];

        // Loop through each character in the string
        for (let i = 0; i < s.length; i++) {
            const char = s[i];
            
            // If the character is a closing bracket
            if (dictionary[char]) {
                // Pop from stack, or use a dummy value if stack is empty
                const topElement = stack.length === 0 ? '#' : stack.pop();
                
                // If the popped element doesn't match the expected opening bracket
                if (topElement !== dictionary[char]) {
                    return false;
                }
            } else {
                // If it's an opening bracket, push it onto the stack
                stack.push(char);
            }
        }

        // If the stack is empty, all brackets were matched correctly
        return stack.length === 0;
    }
}
