function update(){
            $.ajax({
                url: '/temp',
                success: function (data) {
                    var tmp = document.getElementById('cpu_temp')
                    tmp.innerHTML = data[0];
                    if(data[0] >40 ){
                        tmp.style.color = "#d8362a";
                    }else{
                        tmp.style.color = "#4c4c4c";
                    }
                    
                }
            });
        }

window.setInterval(function(){
            update();
        }, 3000);

function get_btn(btn_name){
        $.ajax({
             
                url: btn_name,
                success: function (data) {
                    console.log()
                }
            });
    }
