
function range (start,end){
    start = Number(start) || 0;

    if (end === undefined){
        return function getEnd(end){
            return getRange(start,end);
        };
    }
    else {
        end = Number(end) || 0;
        return getRange(start,end);
    }

    
    function getRange (start,end){
        var arr = [];
        for (let i = start; i <= end; i++){
            
            arr.push(i);

        }

        return arr;
    }

}


console.log(range(3,9));
console.log(range(3,3));


var start3 = range(8);
console.log(start3(8));

