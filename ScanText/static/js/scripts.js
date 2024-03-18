
// =================================================================================================================
// ================================================SLIDE SHOW=======================================================

let slideIndex = 0;

window.addEventListener('DOMContentLoaded', function() {
  showSlides();
  setInterval(showSlides, 4000); // Change image every 4 seconds
});

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");

  if (slides.length > 0 && dots.length > 0) {
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    if (dots.length > 0) {
      dots[slideIndex-1].className += " active";
    }
  }
}
// =================================================================================================================
// ==================================================TIME===========================================================

var curDate = new Date();

                // Ngày hiện tại
                var curDay = curDate.getDate();

                // Tháng hiện tại
                var curMonth = curDate.getMonth() + 1;

                // Năm hiện tại
                var curYear = curDate.getFullYear();
                // Giờ hiện tại
                var curHour = curDate.getHours();

                // Phút hiện tại
                var curMinute = curDate.getMinutes();

                // Gán vào thẻ HTML
                document.getElementById('current-time').innerHTML =curHour + ":" + curMinute + "  " + curDay + "/" + curMonth + "/" + curYear;

// =================================================================================================================
// =================================================================================================================
