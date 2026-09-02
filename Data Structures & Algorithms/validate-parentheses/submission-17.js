class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = []
        const bracketMap = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for (let char of s) {
            if(bracketMap[char]){
                if(bracketMap[char] !== stack.pop())
                    return false

            }
            else {
                stack.push(char)
            }

        }
        return stack.length ===0
    }
}
