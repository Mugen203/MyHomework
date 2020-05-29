const startDay = "07:30";
const endDay = "17:45";

function scheduleMeeting (startTime, durationMinutes){
    if (startTime + durationMinutes <= endDay){
        return console.log(Boolean(true))
    }
    else return console.log(Boolean(false))
};
scheduleMeeting("11:30",60);


