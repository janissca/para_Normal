function isIterable(obj) {
    // checks for null and undefined
    if (obj == null) {
      return false;
    }
    return typeof obj[Symbol.iterator] === 'function';
  }

  function dateParser(date) {
    const time_elems = date.split("T")
    
    console.log(time_elems)

    const full_date = time_elems[0].split("-")
    const full_time = time_elems[1].split(".")

    const year = full_date[0]
    const month = full_date[1]
    const day = full_date[2]

    const time = full_time[0].split(":")
    const hour = time[0]
    const minute = time[1]
    
    return {
      year: year,
      month: month,
      day: day,
      hour: hour,
      minute: minute,
    }
  }

  function formatDate(date){
    const date_obj = dateParser(date)
    const date_string = `${date_obj.day}-${date_obj.month}-${date_obj.year}`
    const time_string = `${date_obj.hour}:${date_obj.minute}`
    const result_date = date_string + " в " + time_string

    return result_date
  }

  module.exports = {
    isIterable,
    dateParser,
    formatDate
};