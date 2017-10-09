function getRandomIntInclusive(max) {
  return Math.floor(Math.random() * (max+1)); //The maximum is inclusive
}
var lastNum = 0;
$(document).ready(function() {
    console.log("ready!");

    var myNum = $("#truckTotal").attr("num")
    console.log(parseInt(myNum));

    $("#finder-btn").click(function() {
        console.log("btn pressed");
        var x = getRandomIntInclusive(parseInt(myNum))
        if(lastNum === x){
            x = x + 1;
        }
        lastNum = x;
        console.log(x);

        // $("#finder-text").html("The {{trucks."+lastNum+".primary_color}} and {{trucks."+lastNum+".secondary_color}} {{trucks."+lastNum+".truck_color.category.category_name}}")

        // -------------
        // $("#finder-text").html('<h2 class="ui header" id="finder-text">The {{trucks.'+lastNum+'.primary_color}} and {{trucks.'+lastNum+'.secondary_color}} {{trucks.'+lastNum+'.truck_color.category.category_name}} </h2>')

        e.preventDefault()
        $.ajax({
            url: '/finder',
            method: 'GET',
            data: $(this).serialize(),
            success: function(serverResponse) {
                // console.log("Received this from server: ", serverResponse)
                $('#finder-text').html(serverResponse)
            }
        })
    })
    // console.log(total_trucks);


});
