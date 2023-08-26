
    /* Allert messsages */
    setTimeout(function () {

            let messages = document.getElementById("msg");
            if(messages != null){
              let alert = new bootstrap.Alert(messages);
              alert.close();
            }
            
        }, 3000);
        
    /* Arrow button script */
    function topFunction() {
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    }
