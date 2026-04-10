class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        let result= []
        for(let i=0; i <temperatures.length; i++){
            for(let j=i; j<temperatures.length; j++) {
                
                if(temperatures[i] < temperatures[j]) {
                    result.push(j-i)
                    break;
                } else if(j === temperatures.length-1){
                    result.push(0)
                }
                

            }
        }
        return result
    }
}


//We have an array of temperatures i in each index
//we return array that contains how many days till warmer day
//based on that current day's temperature