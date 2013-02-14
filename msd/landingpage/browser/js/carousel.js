jq(document).ready(function() {
    
	    jq('#content .carousel').hover(
	        function() {
	            jq(this).find('.carousel-pager-button-prev').toggle();
	            jq(this).find('.carousel-pager-button-next').toggle();
	        }
    	);
    	
	    jq('#content .carousel-pager-tab .carousel-pager-item').hover( function() {
	          jq(this).click();
	      });
	    
	    /*
	     * Fix carousel banner block size to size the imagein it has. Normally Products.Carousel takes height and width from the
	     * carousel settings, but we also have text in the carousel so it won't work for us.
	     */
        jq("#content .carousel-banners").each( function() {
         var banner = jq(this);
         var parent = banner.parent();
         var h = banner.find("img:visible").css("height");
         var w = banner.find("img:visible").css("width");
         banner.css("height", h);
         banner.find(".carousel-banner").css("height", h);
         
         if(parent.hasClass("banner-slideshow-tabbed")) {
             banner.css("width", w);
             parent.find(".carousel-pager").css("height", h);
         }
        });

});

