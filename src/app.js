function maxlength(element, maxvalue){
  var wordCount = element.value.split(/[\s]+/).length;
  if(wordCount > maxvalue){
    var difference = wordCount - maxvalue;
    alert("Sorry, you have input "+wordCount+" words into the " + "text area box you just completed. It can return no more than "+ maxvalue +" words. Please abbreviate " + "your text by at least "+difference+" words");
    return false;
  }
}

function minlength(element, minvalue){
  var wordCount = element.value.split(/[\s]+/).length;
  if(wordCount < minvalue){
    var difference = minvalue - wordCount;
    alert("Sorry, you have input "+wordCount+" words into the " + "text area box you just completed. It must contain "+ minvalue + " words. Please extend your answer by "+difference+" words");
    return false;
  }
}

function mobileOpenNav() {
  var links = document.getElementById("navbar");
  var closeButton = document.getElementById('close_icon');
  links.style.display = "block";
  closeButton.style.display = "block";
}

function mobileCloseNav() {
  var links = document.getElementById("navbar");
  var closeButton = document.getElementById('close_icon');
  links.style.display = "none";
  closeButton.style.display = "none";
}

function initialize(){
  /*var mobileOpenNavButton = document.getElementById('open_icon');
  mobileOpenNavButton.onclick = mobileOpenNav;
  var mobileCloseNavButton = document.getElementById('close_icon');
  mobileCloseNavButton.onclick = mobileCloseNav;*/

  if (document.getElementsByTagName("body")[0].className == "application"){
    var form = document.getElementById("form");
    var textarea1 = document.getElementById("lq1");
    var textarea2 = document.getElementById("lq2");
    form.onsubmit = function (event) {
      maxlength(textarea1, 500);
      maxlength(textarea2, 500);
      minlength(textarea1, 250);
      minlength(textarea2, 250);

    };
    textarea1.onchange = function (event) {
      maxlength(textarea1, 500);
      minlength(textarea1, 250);
    };
    textarea2.onchange = function (event) {
      maxlength(textarea2, 500);
      minlength(textarea2, 250);
    };
  }
}

window.onload = initialize;
