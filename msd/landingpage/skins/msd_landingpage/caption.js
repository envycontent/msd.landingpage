jq(document).ready(function(){
	jq('#text img').jcaption();
	jq('#sidebar img').jcaption({
		copyStyle: true,
		animate: true,
		show: {height: "show"},
		hide: {height: "hide"}
	});


   jq('#slideshow').cycle()


   // perform JavaScript after the document is scriptable. 
   jq(function() { 
    // setup ul.tabs to work as tabs for each div directly under div.panes 
    jq("ul.tabs").tabs("div.panes > div"); 
});
});