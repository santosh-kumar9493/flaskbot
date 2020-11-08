const msg=new SpeechSynthesisUtterance();
msg.volume=1
msg.rate=1
msg.pitch=1
msg.lang="en-UK"



const SpeechRecognition =
  window.webkitSpeechRecognition || window.SpeechRecognition
const recognition = new SpeechRecognition()
recognition.lang = 'en-UK'
recognition.interimResults = false




$(function() {
    
        send_resp=function(prop){
            let  val=$('#userin').val()
            if(val!=''){
                $('#userin').parent('.form').replaceWith(`<span class="form">${val}</span`)
                $.post("message",{key:prop,message:val})
                .done(function(response){
                    $('#chat main').append(response);
                    $(response).ready(function(){
                        voice($(response).text());
                    });
                });
                
                
            }
            else{
                voice("Input cannot be empty");
            }
        }
        
        voice_resp=function(prop){
            recognition.start()
            recognition.onresult = event => {
                var val = event.results[0][0].transcript;
                $('#userin').parent('.form').replaceWith(`<span class="form">${val}</span`)
                $.post("message",{key:prop,message:val})
                .done(function(response){
                    $('#chat main').append(response);
                    $(response).ready(function(){
                        voice($(response).text())
                    });
                    $("#userin").stop().animate({ scrollTop: $("#userin")[0].scrollHeight}, 1000);
                })
            }
            
        }
        voice=function(info){
            msg.text=info;
            speechSynthesis.speak(msg)
        }
});