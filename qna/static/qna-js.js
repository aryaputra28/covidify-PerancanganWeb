$(document).ready( function () {
    $(".btn-qna").on("mouseleave", function(){
    $(this).css("background-color", "#232065");
    $(this).css("border-color", "blue");
    $(this).css("color", "#white");

  });
    $(".btn-qna").on("mouseenter", function(){
    $(this).css("background-color", "#DCCFEE");
    $(this).css("color", "#black");
    });
    $("label.switch").click(function() {
    $("p").toggleClass("light-font");
    $("body").toggleClass("dark-bg");
    $(".card-qna").toggleClass("qna-container-darkmode");
    $(".btn-qna2").toggleClass("btn-qna3");
    console.log($(".small"))
    });
    $(".accd").on("click", function(){
        console.log("masuk");
        var acc = $("#accord-hide");
        if(acc.attr("class").includes("active")){
            acc.removeClass("active")
            acc.css("display", "block");
        }
        else{
            acc.addClass("active")
            acc.css("display", "none");
        }
    });
    $.ajax({
        url: "/dataqna",
        success: function(data) {
            console.log("test")
            var result = '<tr>';
            for(var i = 0; i < data.length; i++) {
                var obj = data[i];
                var currentDate = JSON.stringify(obj.fields.time);
                currentDate = new Date(JSON.parse(currentDate));
                var date = currentDate.toString();
                date = date.substring(0,21);
                console.log(obj.pk)
                result += '<tr><td><div class="card card-qna"><div class=" border-bottom border-light"><b>'
                    +obj.fields.penanya+
                    '</b> </div><div>'
                        +obj.fields.pertanyaan+
                        '</div><div class="small">'
                            +obj.fields.location+' on '+ date+ ' | ' +obj.fields.email+
                            '</div><nav class="navbar navbar-inverse"><div class="nav"> </div><div class="nav"><a class="btn btn-qna2" href="/balas/'+obj.pk+ '/" role="button">Open</a></div></nav></div><br></td></tr>';   
                          
                          
            }
            $('#isiqna').append(result);
        }
    });
    $.ajax({
        url: "/datakomen",
        success: function(data) {
            console.log("komen");
            var result = '<tr>';
            var comment = document.getElementById("komen").innerHTML;
            console.log("comment"+comment)
            for(var i = 0; i < data.length; i++) {
                var obj = data[i];
                var currentDate = JSON.stringify(obj.fields.time);
                currentDate = new Date(JSON.parse(currentDate));
                var date = currentDate.toString();
                date = date.substring(0,21);
                console.log(obj);
                console.log(obj.pk)
                if (obj.fields.tanya == comment){
                    result += '<tr class=" table border-0"><td><div><div class="card card-komen"><div class="border-bottom border-dark"><b>'
                    +obj.fields.pengomentar+
                    '</b> </div><div class=>'
                    +obj.fields.komen+
                    '</div><div class= "small">'
                    +obj.fields.location+' on '+date+' | '+obj.fields.email+
                    '</div></div></div></td> </tr>'
                }
            };
            $('#isikomen').append(result);
        }
    });
});