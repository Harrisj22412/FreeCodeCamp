//Cid argument is a 2D array
//Return should be a value (key)


var denominations = [
    {name: "ONE HUNDREND", value: 100.00},
    {name: "TWENTY", value: 20.00},
    {name: "TEN", value: 10.00},
    {name: "FIVE", value: 5.00},
    {name: "ONE", value: 1.00},
    {name: "QUARTER", value: 0.25},
    {name: "DIME", value: 0.10},
    {name: "NICKEL", value: 0.05},
    {name: "PENNIES", value: 0.01}
];

function checkCashRegister(price, cash, cid) {
    //1. We want to calculate the change that we owe the customer.
    var change = cash - price ;
    //2. Then we need to calucalte how much money is in the draw.
    //3. Then we are going to give the accumulator a start value. 
    var totalCid = cid.reduce(function (acc, next){
        //4. We are iterating through these 2D arrays
        return acc + next[1]
    }, 0.0);

    if (totalCid < change){
        return "Insufficient Funds";
    } else if(totalCid === change){
        return 'Closed';
    }
    //4. We must reverse the 2D array to make our object into a descending 
order in order for it to work. 
    cid = cid.reverse();

    var result = denominations.reduce(function(acc, next, index){
        if(change >= next.value){
           var currentValue = 0.0;
           //5. We are going to keep looping until change is greater than or 
equal to that value. 
           while(change >= next.value && cid[index][1] > next.value) {
            currentValue += next.value;
            change -= next.value;
            //This makes sure that our decimal places are the most accurate as 
it can be. 
            change = Math.round(change * 100) / 100;
            //Then we need to update our cash in draw.
            cid[index][1] -= next.value;

           }
           acc.push([next.name, currentValue]);
           return acc;

        } else {
           return acc; 
        }
        //5. We are going to give the accumlator the starting value of an empty 
array. 
    },[]);

    return result.length > 0 && change === 0 ? result : "Insufficient Funds";
  }
  
  checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1]
, ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], 
["ONE HUNDRED", 100]]);
