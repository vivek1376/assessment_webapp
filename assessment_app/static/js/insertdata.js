document.addEventListener("DOMContentLoaded", function() {
    // console.log("hello from insertdata.js!!!")

    document.getElementById("insertdata").addEventListener('submit',
        function (event) {
            event.preventDefault();
            console.log("submit button clicked!!!");

            var roledropdown_obj = document.getElementById('roledropdown');
            var roleid = parseInt(roledropdown_obj.options[roledropdown_obj.selectedIndex].value);

            var postdata = {
                'username': document.getElementById('usernameinput').value,
                'roleid': roleid
            };

            axios.post('/insertdata', postdata, {
                headers:{
                    'Content-Type': 'application/json'
                }
            }).then(function (response) {
                console.log("post response:", response['data']);

                statusmsg = response['data']['statusmsg']
                document.getElementById("statusmsg").innerText = statusmsg;

            }).catch(function (error) {
                console.log(error);
            });
        });
});

