
var type=new Typed("#about_us",
{
	strings:["hello","Welcome, visitors to the site We always strive to create a generation of programmers capable of creating miracles"],
	typeSpeed:50
	}
)





 
var set=setInterval(function(){
    var kids_count= parseInt($("#kids_count").text());
            $("#kids_count").text((kids_count+1))
            if($("#kids_count").text()>=295){
                     clearInterval(set)
                 }
    },300)
    
 
var m=setInterval(function(){
        var men_count= parseInt($("#men_count").text());
                $("#men_count").text((men_count+1))
                if($("#men_count").text()>=178){
                         clearInterval(m)
                     }
        },300)
            
 
var h=setInterval(function(){
            var womans_count= parseInt($("#womans_count").text());
                    $("#womans_count").text((womans_count+1))
                    if($("#womans_count").text()>=145){
                            clearInterval(h)
                         }
            },300)
                    