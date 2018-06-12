
function checkNotification(title,message) {
    var options ={
        body:'tbody',
        data:'tdata'
    };
    if (!("Notification" in window)) {
        alert("This browser does not support desktop notification");
    }
    // check whether notification permissions have alredy been granted
    else if (Notification.permission === "granted") {
        // If it's okay let's create a notification
        var notify = new Notification(title,{dir:'auto',lang:'zh-CN',icon:'/static/img/curious.ico',body:message});
        notify.onshow = function () {
                    setTimeout(function(){
                        notify.close();
                    },600000)
                };
    }
    // Otherwise, ask the user for permission
    else if (Notification.permission !== 'denied') {
        Notification.requestPermission(function (permission) {
            // If the user accepts, let's create a notification
            if (permission === "granted") {
                new Notification("Request granted!");
            }
        });
    }
}