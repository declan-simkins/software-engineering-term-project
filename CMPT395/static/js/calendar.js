function startup(default_title, default_color) {
  // Change calendars from being stacked to being in front of one another
  var calendars = document.getElementsByClassName("calendar");
  var total_height = 0;
  var max_height = 0;
  for (var i = 0; i < calendars.length; i++) {
    calendars[i].style.top = (0 - total_height).toString() + "px";
    total_height += calendars[i].clientHeight;
    if (calendars[i].clientHeight > max_height) {
      max_height = calendars[i].clientHeight;
    }
    calendars[i].style.visibility = "hidden";
  }
  
  // Change height of pagewrap to accomodate for calendars no longer being
  // stacked
  var header_height = document.getElementById("main-header").clientHeight;
  var pagewrap = document.getElementById("pagewrap");
  var pagewrap_height = pagewrap.clientHeight;
  pagewrap.style.height = (pagewrap_height - total_height) + (max_height + header_height)  + "px";
  
  switch_calendar(default_title, default_color);
}

function toggle_popup(elemId) {
    /*
      Toggles visibility of an html element
      Pre: An html element with a uniquely assigned id
      Post: html elements visibility will be toggled
      Param: elemId: String containing ID of element to be toggled
      Return: None
      Side Effects: Element identified by elemId will have its
        visibility toggled
    */
    elem = document.getElementById(elemId);
    if (elem.style.visibility == "visible") {
        elem.style.visibility = "hidden";
    }
    else {
        elem.style.visibility = "visible";
    }
}

function switch_calendar(new_calendar_title, new_calendar_color) {
  set_current_classroom(new_calendar_title, new_calendar_color);
  var new_calendar = document.getElementById("js-" + new_calendar_title + "-calendar");
  var calendars = document.getElementsByClassName("calendar");
  
  for (var i = 0; i < calendars.length; i++) {
    if (calendars[i].style.visibility == "visible") {
      calendars[i].style.visibility = "hidden";
    }
  }
  new_calendar.style.visibility = "visible";
}

function set_current_classroom(classroom_title, classroom_color) {
  var signup_class = document.getElementById("id_classroom");
  var class_list = document.getElementById("js-class-list");

  signup_class.value = classroom_title;
  class_list.style.backgroundColor = classroom_color.toLowerCase();
}

function toggle_signup(day, date, start, end, formatted_date) {
  // Populate form fields
  var signup_date = document.getElementById("js-signup-date");
  var signup_day = document.getElementById("js-signup-day");
  signup_date.innerHTML = date;
  signup_day.innerHTML = day;
  
  var signup_class = document.getElementById("id_classroom");
  var signup_start = document.getElementById("id_start_time");
  var signup_end = document.getElementById("id_end_time");
  
  signup_start.value = start;
  signup_end.value = end;
  
  var hidden_date = document.getElementById("js-signup-hidden-date");
  hidden_date.value = formatted_date;
  // Toggle visibility
  toggle_popup("sign-up-overlay");
}
