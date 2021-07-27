$(document).ready(function() {
    // executes when HTML-Document is loaded and DOM is ready
   // breakpoint and up  
        const menu = $('#portal-globalnav-collapse');

        $(document).mouseup(e => {
          if (!menu.is(e.target) // if the target of the click isn't the container...
          && menu.has(e.target).length === 0) // ... nor a descendant of the container
          {
            menu.removeClass('activated');
            $('.show-nav').removeClass('show-nav');
            $(".mask-menu").removeClass("in");
         }
        });
         // when you hover a toggle show-nav its dropdown menu
         $(".has_subtree > a").click(function () {
           if(!$("#portal-globalnav .show-nav").length > 0){
             $(menu).toggleClass("activated");
             $(".mask-menu").toggleClass("in");
           }
            $(this).parent().toggleClass("show-nav");
            $(this).parent().find(".show-nav").toggleClass("show-nav");
            $(this).parent().siblings(".show-nav").toggleClass("show-nav")
            console.log($(this).parent().siblings(".show-nav"))
      
            $(this).parent().find(".activated").toggleClass(".activated");
             if(!$("#portal-globalnav .show-nav").length > 0){
               $(menu).toggleClass("activated");
               $(".mask-menu").toggleClass("in");

            }
            return false
          });       
   });