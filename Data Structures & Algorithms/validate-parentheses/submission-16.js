class Solution {
  /**
   * @param {string} s
   * @return {boolean}
   */
  isValid(s) {
    let checker = [];

    for (let char of s) {
      if (char === '(' || char === '[' || char === '{') {
        checker.push(char);
      } else if (char === ')' || char === ']' || char === '}') {

        if (checker.length === 0) return false; // 🔑 nothing to match

        const last = checker.pop();

        if (
          (char === ')' && last !== '(') ||
          (char === ']' && last !== '[') ||
          (char === '}' && last !== '{')
        ) {
          return false; // 🔑 mismatched pair
        }
      }
    }

    return checker.length === 0;
  }
}
