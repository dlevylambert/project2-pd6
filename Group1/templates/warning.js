$(document).ready(function(){

    function addWarning(){
	if( $('#forms').val().length == 0 ) {
	    $('#forms').parents('p').addClass('warning');
	}	
    }
    
    $('#search').hover(addWarning());
    
});
		  
