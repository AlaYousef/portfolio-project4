function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
setTimeout(function () {
  let messages = document.getElementById('msg');
   
  let alert = new bootstrap.Alert(messages);
      }, 2500);
  
  

  